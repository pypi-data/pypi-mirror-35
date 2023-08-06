# -*- coding: utf-8 -*-
"""Main tagger class
"""

import math
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

    def __init__(self, # pylint: disable=too-many-arguments
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
                 optimizer={
                     'optim': 'Adam',
                     'learning_rate': 1e-3
                 },
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
            'optimizer': optimizer
        }
        self._model = _model
        self._optimizer = _optimizer
        self._word_to_ix = _word_to_ix
        self._ix_to_word = _ix_to_word
        self._tag_to_ix = _tag_to_ix
        self._ix_to_tag = _ix_to_tag

    def get_params(self, deep=True):
        """Get params for scikit-learn compatible"""
        params = self.params
        if deep:
            params['_model'] = self._model.state_dict() if self._model is not None else None
            params['_optimizer'] = self._optimizer.state_dict() if self._optimizer is not None else None
            params['_word_to_ix'] = self._word_to_ix
            params['_ix_to_word'] = self._ix_to_word
            params['_tag_to_ix'] = self._tag_to_ix
            params['_ix_to_tag'] = self._ix_to_tag
        return params

    def set_params(self, **parameters):
        """Set params for scikit-learn compatible"""
        for k, v in parameters.items():
            if k in self.params:
                self.params[k] = v
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
        elif device in ('gpu', 'cuda'):
            return torch.device('cuda')
        else:
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
            rnn_type=rnn_type
        ).to(self._get_device())

        if optimizer['optim'].upper() == 'ADAM':
            optimizer = optim.Adam(
                model.parameters(),
                lr=optimizer.get('learning_rate', 1e-3),
                weight_decay=weight_decay
            )
        elif optimizer['optim'].upper() == 'SGD':
            optimizer = optim.SGD(
                model.parameters(),
                lr=optimizer.get('learning_rate', 1e-2),
                weight_decay=weight_decay,
                momentum=optimizer.get('momentum', 0)
            )

        self._model = model
        self._optimizer = optimizer
    
    def fit(self, X, y, X_dev=None, y_dev=None):
        """Fit the model"""

        assert len(X) > 0, 'X must size > 0'
        assert len(y) > 0, 'y must size > 0'
        assert len(X) == len(y), 'X must size equal to y'

        # Autommatic build vocabulary
        if self._word_to_ix is None or len(self._word_to_ix) <= 0:
            vocabulary = build_vocabulary(X, y)
            self._word_to_ix = vocabulary['word_to_ix']
            self._ix_to_word = vocabulary['ix_to_word']
            self._tag_to_ix = vocabulary['tag_to_ix']
            self._ix_to_tag = vocabulary['ix_to_tag']

        epochs = self.params['epochs']
        verbose = self.params['verbose']
        batch_size = self.params['batch_size']

        word_to_ix = self._word_to_ix
        tag_to_ix = self._tag_to_ix
        ix_to_tag = self._ix_to_tag

        self.apply_params()
        model, optimizer = self._model, self._optimizer

        # Check predictions before training
        with torch.no_grad():
            precheck_sent = prepare_sequence(X[0], word_to_ix)
            precheck_sent = torch.stack([precheck_sent])
            precheck_sent = precheck_sent.to(self._get_device())
            _, p = model(precheck_sent)
            assert len([ix_to_tag[tag_to_ix[t]] for t in y[0]]) == len(p[0]), \
                'checking before training error'

        # Make sure prepare_sequence from earlier in the LSTM section is loaded
        for epoch in range(epochs):
            pbar = range(math.ceil(len(X) / batch_size))
            losses = []
            if verbose > 0:
                pbar = tqdm(pbar, ncols=0)
                pbar.set_description('epoch: {}/{} loss: {:.4f}'.format(epoch + 1, epochs, 0))
            for _ in pbar:

                xb, yb, lb = next(batch_flow(X, y, word_to_ix, tag_to_ix, batch_size))
                xb = xb.to(self._get_device())
                yb = yb.to(self._get_device())
                lb = lb.to(self._get_device())

                # Step 1. Remember that Pytorch accumulates gradients.
                # We need to clear them out before each instance
                model.zero_grad()

                # Step 2. Run our forward pass.
                loss = model.neg_log_likelihood(xb, yb, lb)
                losses.append(loss.item())

                # Step 3. Compute the loss, gradients, and update the parameters by
                # calling optimizer.step()
                loss.backward()
                nn.utils.clip_grad_value_(model.parameters(), 5.)
                optimizer.step()
                if verbose > 0:
                    pbar.set_description('epoch: {}/{} loss: {:.4f}'.format(epoch + 1, epochs, np.mean(losses)))
            # train_score = self.score(X, y)
            # test_score = None
            # if X_dev is not None:
            #     test_socre= self.score(X_dev, y_dev)
            # if test_score is None:
            #     print('train: {:.2f}'.format(train_score))
            # else:
            #     print('train: {:.2f}, test: {:.2f}'.format(train_score, test_score))

    def predict(self, X, batch_size=None, verbose=0):
        """Predict tags"""
        assert len(X) > 0, 'predict empty'
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
                for l, tags in zip(lens, predicts):
                    tags = [ix_to_tag[i] for i in tags[:l]]
                    ret.append(tags)
        return ret

    def score(self, X, y, verbose=0):
        """Calculate NER F1"""
        preds = self.predict(X, verbose=verbose)
        scores = []
        pbar = zip(preds, y)
        if verbose > 0:
            pbar = tqdm(pbar, ncols=0, total=len(y))
        for pred, yy in pbar:
            pset = extrat_entities(pred)
            rset = extrat_entities(yy)
            pset = set(pset)
            rset = set(rset)
            inter = pset.intersection(rset)
            precision = len(inter) / len(pset) if len(pset) > 0 else 1
            recall = len(inter) / len(rset) if len(rset) > 0 else 1
            f1score = 0
            if precision + recall > 0:
                f1score = 2 * ((precision * recall) / (precision + recall))
            scores.append(f1score)
        return np.mean(scores)
