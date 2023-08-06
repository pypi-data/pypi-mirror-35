# -*- coding: utf-8 -*-
# Based https://pytorch.org/tutorials/beginner/nlp/advanced_tutorial.html
# Modified by InfinityFuture

import math
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
from sklearn.base import BaseEstimator
import numpy as np

from torch_tagger.rnn_crf import RNN_CRF
from torch_tagger.utils import build_vocabulary, prepare_sequence, batch_flow, DEVICE
from torch_tagger.utils import extrat_entities, pad_seq

class Tagger(BaseEstimator):
    """scikit-learn compatible Tagger"""

    def __init__(
        self,
        embedding_dim=64,
        hidden_dim=32,
        learning_rate=1e-3,
        weight_decay=1e-6,
        epochs=10,
        verbose=1,
        batch_size=32,
        device='auto',
        embedding_dropout_p=0.1,
        rnn_dropout_p=0.1,
        bidirectional=True,
        rnn_type='lstm',
        num_layers=1,
        model=None,
        optimizer=None,
        word_to_ix={},
        ix_to_word={},
        tag_to_ix={},
        ix_to_tag={},
        ):
        """init"""
        self.params = {
            'embedding_dim': embedding_dim,
            'hidden_dim': hidden_dim,
            'learning_rate': learning_rate,
            'weight_decay': weight_decay,
            'epochs': epochs,
            'verbose': verbose,
            'batch_size': batch_size,
            'device': device,
            'embedding_dropout_p': embedding_dropout_p,
            'rnn_dropout_p': rnn_dropout_p,
            'bidirectional': bidirectional,
            'rnn_type': rnn_type,
            'num_layers': num_layers
        }
        self.model = model
        self.optimizer = optimizer
        self.word_to_ix=  word_to_ix
        self.ix_to_word = ix_to_word
        self.tag_to_ix = tag_to_ix
        self.ix_to_tag = ix_to_tag

    def get_params(self, deep=True):
        """Get params for scikit-learn compatible"""
        params = self.params
        if deep:
            params['model'] = self.model.state_dict() if self.model is not None else None
            params['optimizer'] = self.optimizer.state_dict() if self.optimizer is not None else None
            params['word_to_ix'] = self.word_to_ix
            params['ix_to_word'] = self.ix_to_word
            params['tag_to_ix'] = self.tag_to_ix
            params['ix_to_tag'] = self.ix_to_tag
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
            'model': self.model.state_dict() if self.model is not None else None,
            'optimizer': self.optimizer.state_dict() if self.optimizer is not None else None,
            'word_to_ix': self.word_to_ix,
            'ix_to_word': self.ix_to_word,
            'tag_to_ix': self.tag_to_ix,
            'ix_to_tag': self.ix_to_tag
        }
        return state
    
    def __setstate__(self, state):
        """Get state for pickle"""
        self.params = state['params']
        if state['model'] is not None:
            self.word_to_ix = state['word_to_ix']
            self.ix_to_word = state['ix_to_word']
            self.tag_to_ix = state['tag_to_ix']
            self.ix_to_tag = state['ix_to_tag']
            self.apply_params()
            self.model.load_state_dict(state['model'])
            self.optimizer.load_state_dict(state['optimizer'])

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
        learning_rate = self.params['learning_rate']
        weight_decay = self.params['weight_decay']
        embedding_dropout_p = self.params['embedding_dropout_p']
        rnn_dropout_p = self.params['rnn_dropout_p']
        bidirectional = self.params['bidirectional']
        rnn_type = self.params['rnn_type']
        num_layers = self.params['num_layers']

        word_to_ix = self.word_to_ix
        tag_to_ix = self.tag_to_ix

        model = RNN_CRF(
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

        optimizer = optim.Adam(
            model.parameters(),
            lr=learning_rate,
            weight_decay=weight_decay
        )

        self.model = model
        self.optimizer = optimizer
    
    def fit(self, X, y):
        """Fit the model"""

        assert len(X) > 0, 'X must size > 0'
        assert len(y) > 0, 'y must size > 0'
        assert len(X) == len(y), 'X must size equal to y'

        # Autommatic build vocabulary
        if len(self.word_to_ix) <= 0:
            vocabulary = build_vocabulary(X, y)
            self.word_to_ix = vocabulary['word_to_ix']
            self.ix_to_word = vocabulary['ix_to_word']
            self.tag_to_ix = vocabulary['tag_to_ix']
            self.ix_to_tag = vocabulary['ix_to_tag']

        epochs = self.params['epochs']
        verbose = self.params['verbose']
        batch_size = self.params['batch_size']

        word_to_ix = self.word_to_ix
        tag_to_ix = self.tag_to_ix
        ix_to_tag = self.ix_to_tag

        self.apply_params()
        model, optimizer = self.model, self.optimizer

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
                optimizer.step()
                if verbose > 0:
                    pbar.set_description('epoch: {}/{} loss: {:.4f}'.format(epoch + 1, epochs, np.mean(losses)))
    
    def predict(self, X, batch_size=32, verbose=0):
        """Predict tags"""
        assert len(X) > 0, 'predict empty'
        model = self.model
        word_to_ix = self.word_to_ix
        ix_to_tag = self.ix_to_tag
        
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
            f1 = 0
            if precision + recall > 0:
                f1 = 2 * ((precision * recall) / (precision + recall))
            scores.append(f1)
        return np.mean(scores)
