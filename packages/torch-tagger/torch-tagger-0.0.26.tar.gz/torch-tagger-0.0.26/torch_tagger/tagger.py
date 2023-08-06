# -*- coding: utf-8 -*-
"""Main tagger class
"""

import os
import math
import pickle
import torch
from torch import nn
from torch import optim
from tqdm import tqdm
from sklearn.base import BaseEstimator
import numpy as np

from torch_tagger.rnn_crf import RNNCRF
from torch_tagger.utils import build_vocabulary, prepare_sequence, batch_flow, DEVICE
from torch_tagger.utils import extrat_entities, pad_seq

class Tagger(BaseEstimator):
    """scikit-learn compatible Tagger"""

    def __init__(self, # pylint: disable=too-many-arguments,too-many-locals
                 embedding_dim=32,
                 hidden_dim=32,
                 weight_decay=0.0,
                 epochs=10,
                 verbose=1,
                 batch_size=32,
                 device='auto',
                 embedding_dropout_p=0.0,
                 rnn_dropout_p=0.0,
                 bidirectional=True,
                 rnn_type='lstm',
                 num_layers=1,
                 optimizer='Adam',
                 learning_rate=None,
                 learning_rate_decay=0,
                 embedding_trainable=True,
                 _model=None,
                 _optimizer=None,
                 _word_to_ix=None,
                 _ix_to_word=None,
                 _tag_to_ix=None,
                 _ix_to_tag=None):
        """init"""
        self.params = {
            'embedding_dim': embedding_dim,
            'hidden_dim': hidden_dim,
            'weight_decay': weight_decay,
            'epochs': epochs,
            'verbose': verbose,
            'batch_size': batch_size,
            'device': device,
            'embedding_dropout_p': embedding_dropout_p,
            'rnn_dropout_p': rnn_dropout_p,
            'bidirectional': bidirectional,
            'rnn_type': rnn_type,
            'num_layers': num_layers,
            'optimizer': optimizer,
            'learning_rate': learning_rate,
            'learning_rate_decay': learning_rate_decay,
            'embedding_trainable': embedding_trainable,
        }
        self._model = _model
        self._optimizer = _optimizer
        self._word_to_ix = _word_to_ix
        self._ix_to_word = _ix_to_word
        self._tag_to_ix = _tag_to_ix
        self._ix_to_tag = _ix_to_tag

    def _get_learning_rate(self):
        optimizer = self.params['optimizer']
        learning_rate = self.params['learning_rate']
        if learning_rate is not None:
            return learning_rate
        if optimizer.upper() == 'SGD':
            return 1e-2
        if optimizer.upper() == 'ADAM':
            return 1e-3
        return 1e-3

    def get_params(self, deep=True):
        """Get params for scikit-learn compatible"""
        params = self.params
        if deep:
            params['_model'] = self._model.state_dict() if self._model is not None else None
            params['_optimizer'] = self._optimizer.state_dict() \
                if self._optimizer is not None else None
            params['_word_to_ix'] = self._word_to_ix
            params['_ix_to_word'] = self._ix_to_word
            params['_tag_to_ix'] = self._tag_to_ix
            params['_ix_to_tag'] = self._ix_to_tag
        return params

    def set_params(self, **parameters):
        """Set params for scikit-learn compatible"""
        for key, value in parameters.items():
            if key in self.params:
                self.params[key] = value
        return self

    def __getstate__(self):
        """Get state for pickle"""
        state = {
            'params': self.params,
            '_model': self._model.state_dict() if self._model is not None else None,
            '_optimizer': self._optimizer.state_dict() if self._optimizer is not None else None,
            '_word_to_ix': self._word_to_ix,
            '_ix_to_word': self._ix_to_word,
            '_tag_to_ix': self._tag_to_ix,
            '_ix_to_tag': self._ix_to_tag
        }
        return state

    def __setstate__(self, state):
        """Get state for pickle"""
        self.params = state['params']
        if state['_model'] is not None:
            self._word_to_ix = state['_word_to_ix']
            self._ix_to_word = state['_ix_to_word']
            self._tag_to_ix = state['_tag_to_ix']
            self._ix_to_tag = state['_ix_to_tag']
            self.apply_params()
            self._model.load_state_dict(state['_model'])
            self._optimizer.load_state_dict(state['_optimizer'])

    def _get_device(self):
        """Get device to predict or train"""
        device = self.params['device']
        if device == 'auto':
            return DEVICE
        if device in ('gpu', 'cuda'):
            return torch.device('cuda')
        return torch.device('cpu')

    def apply_params(self):
        """Apply params and build RNN-CRF model"""

        embedding_dim = self.params['embedding_dim']
        hidden_dim = self.params['hidden_dim']
        weight_decay = self.params['weight_decay']
        embedding_dropout_p = self.params['embedding_dropout_p']
        rnn_dropout_p = self.params['rnn_dropout_p']
        bidirectional = self.params['bidirectional']
        rnn_type = self.params['rnn_type']
        num_layers = self.params['num_layers']
        optimizer = self.params['optimizer']
        embedding_trainable = self.params['embedding_trainable']

        word_to_ix = self._word_to_ix
        tag_to_ix = self._tag_to_ix

        model = RNNCRF(
            len(word_to_ix),
            tag_to_ix,
            embedding_dim,
            hidden_dim,
            num_layers=num_layers,
            bidirectional=bidirectional,
            device=self._get_device(),
            embedding_dropout_p=embedding_dropout_p,
            rnn_dropout_p=rnn_dropout_p,
            rnn_type=rnn_type,
            embedding_trainable=embedding_trainable
        ).to(self._get_device())

        if optimizer.upper() == 'ADAM':
            optimizer = optim.Adam(
                model.parameters(),
                lr=self._get_learning_rate(),
                weight_decay=weight_decay
            )
        elif optimizer.upper() == 'SGD':
            optimizer = optim.SGD(
                model.parameters(),
                lr=self._get_learning_rate(),
                weight_decay=weight_decay,
                momentum=0.9
            )

        self._model = model
        self._optimizer = optimizer

    def fit(self, # pylint: disable=invalid-name,too-many-arguments,too-many-locals,too-many-statements,too-many-branches
            X, y,
            X_dev=None, y_dev=None,
            save_best=None,
            pretrained_embedding=None):
        """Fit the model"""

        assert len(X) >= self.params['batch_size'], 'X must size >= batch_size'
        assert len(y) >= self.params['batch_size'], 'y must size >= batch_size'
        assert len(X) == len(y), 'X must size equal to y'

        # Autommatic build vocabulary
        if self._word_to_ix is None and self._tag_to_ix is None:
            vocabulary = build_vocabulary(X, y)
            self._word_to_ix = vocabulary['word_to_ix']
            self._ix_to_word = vocabulary['ix_to_word']
            self._tag_to_ix = vocabulary['tag_to_ix']
            self._ix_to_tag = vocabulary['ix_to_tag']
        elif self._word_to_ix is None:
            vocabulary = build_vocabulary(X, y)
            self._word_to_ix = vocabulary['word_to_ix']
            self._ix_to_word = vocabulary['ix_to_word']
        elif self._tag_to_ix is None:
            vocabulary = build_vocabulary(X, y)
            self._tag_to_ix = vocabulary['tag_to_ix']
            self._ix_to_tag = vocabulary['ix_to_tag']

        epochs = self.params['epochs']
        verbose = self.params['verbose']
        batch_size = self.params['batch_size']
        learning_rate_decay = self.params['learning_rate_decay']

        word_to_ix = self._word_to_ix
        tag_to_ix = self._tag_to_ix
        ix_to_tag = self._ix_to_tag

        self.apply_params()
        model, optimizer = self._model, self._optimizer
        if pretrained_embedding is not None:
            model.init_embedding(pretrained_embedding)

        # Check predictions before training
        with torch.no_grad():
            precheck_sent = prepare_sequence(X[0], word_to_ix)
            precheck_sent = torch.stack([precheck_sent])
            precheck_sent = precheck_sent.to(self._get_device())
            _, pred = model(precheck_sent)
            assert len([ix_to_tag[tag_to_ix[t]] for t in y[0]]) == len(pred[0]), \
                'checking before training error'

        if learning_rate_decay > 0:
            lr_lambda = lambda epoch: self._get_learning_rate() / (1 + epoch * learning_rate_decay)
            scheduler = torch.optim.lr_scheduler.LambdaLR(
                optimizer,
                lr_lambda=[lr_lambda]
            )

        last_best = -9999.
        # Make sure prepare_sequence from earlier in the LSTM section is loaded
        for epoch in range(epochs):
            pbar = range(math.ceil(len(X) / batch_size))
            losses = []
            if verbose > 0:
                pbar = tqdm(pbar, ncols=0)
                pbar.set_description('epoch: {}/{} loss: {:.4f}'.format(epoch + 1, epochs, 0))
            for _ in pbar:

                x_b, y_b, l_b = next(batch_flow(X, y, word_to_ix, tag_to_ix, batch_size))
                x_b = x_b.to(self._get_device())
                y_b = y_b.to(self._get_device())
                l_b = l_b.to(self._get_device())

                # Step 1. Remember that Pytorch accumulates gradients.
                # We need to clear them out before each instance
                model.zero_grad()

                # Step 2. Run our forward pass.
                loss = model.neg_log_likelihood(x_b, y_b, l_b)
                losses.append(loss.item())

                # Step 3. Compute the loss, gradients, and update the parameters by
                # calling optimizer.step()
                loss.backward()
                nn.utils.clip_grad_value_(model.parameters(), 5.)
                optimizer.step()
                if verbose > 0:
                    pbar.set_description(
                        'epoch: {}/{} loss: {:.4f}'.format(
                            epoch + 1, epochs, np.mean(losses)
                        )
                    )
            train_score = self.score(X, y)
            test_score = None
            if X_dev is None:
                if verbose > 0:
                    print('train: {:.4f}'.format(train_score))
            else:
                test_score = self.score(X_dev, y_dev)
                if verbose > 0:
                    print('train: {:.4f}, test: {:.4f}'.format(train_score, test_score))
                if isinstance(save_best, str) and test_score > last_best:
                    print('save best')
                    last_best = test_score
                    save_dir = os.path.realpath(os.path.dirname(save_best))
                    if not os.path.exists(save_dir):
                        os.makedirs(save_dir)
                    with open(save_best, 'wb') as fobj:
                        pickle.dump(self, fobj)
            if learning_rate_decay > 0:
                scheduler.step()

    def predict(self, X, batch_size=None, verbose=0): # pylint: disable=invalid-name,too-many-locals
        """Predict tags"""
        model = self._model
        word_to_ix = self._word_to_ix
        ix_to_tag = self._ix_to_tag
        if batch_size is None:
            batch_size = self.params['batch_size']

        # Check predictions after training
        ret = []
        with torch.no_grad():

            batch_total = math.ceil(len(X) / batch_size)

            pbar = range(batch_total)
            if verbose > 0:
                pbar = tqdm(pbar, ncols=0)
            for i in pbar:
                x_batch = X[i * batch_size : (i + 1) * batch_size]

                max_len = np.max([len(t) for t in x_batch])
                lens = [len(x) for x in x_batch]
                x_batch = [pad_seq(x, max_len) for x in x_batch]
                x_batch = [
                    prepare_sequence(sent, word_to_ix)
                    for sent in x_batch
                ]

                sent = torch.stack(x_batch)
                sent = sent.to(self._get_device())
                _, predicts = model(sent)
                for tag_len, tags in zip(lens, predicts):
                    tags = [ix_to_tag[i] for i in tags[:tag_len]]
                    ret.append(tags)
        return ret

    def score(self, X, y, verbose=0): # pylint: disable=invalid-name,too-many-locals
        """Calculate NER F1
        Based CONLL 2003 standard
        """
        preds = self.predict(X, verbose=verbose)
        scores = []
        pbar = zip(preds, y)
        if verbose > 0:
            pbar = tqdm(pbar, ncols=0, total=len(y))
        for pred, y_true in pbar:
            pset = extrat_entities(pred)
            rset = extrat_entities(y_true)
            pset = set(pset)
            rset = set(rset)
            inter = pset.intersection(rset)
            precision = len(inter) / len(pset) if pset else 1
            recall = len(inter) / len(rset) if rset else 1
            f1score = 0
            if precision + recall > 0:
                f1score = 2 * ((precision * recall) / (precision + recall))
            scores.append(f1score)
        return np.mean(scores)
