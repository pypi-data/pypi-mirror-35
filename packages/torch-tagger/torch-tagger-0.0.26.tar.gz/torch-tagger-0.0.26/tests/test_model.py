# -*- coding: utf-8 -*-
"""Test RNNCRF"""

import torch
import numpy as np
from torch_tagger.rnn_crf import RNNCRF
# from torch_tagger.utils import sequence_mask

def same(amat, bmat):
    """Test two matrix is same"""
    return np.abs(np.sum(np.sum(amat - bmat))) < 1e-6

def test_model(): # pylint: disable=too-many-locals
    """Test model entry"""
    device = torch.device('cpu')
    vocab_size = 10
    tag_to_ix = {'<START>': 0, '<STOP>': 1}
    embedding_dim = 10
    hidden_dim = 10

    try:
        model = RNNCRF(
            vocab_size,
            tag_to_ix,
            embedding_dim,
            hidden_dim,
            device=device,
            rnn_type='unk'
        )
    except Exception as err: # pylint: disable=broad-except
        assert str(err) == 'Invalid rnn_type'

    model = RNNCRF(
        vocab_size,
        tag_to_ix,
        embedding_dim,
        hidden_dim,
        device=device
    )
    # feats_batch dim: [batch_size, seq_len, target_dim]
    # lengths_batch dim: [batch_size]
    batch_size, seq_len, target_dim = 20, 40, 30
    feats = torch.randn(batch_size, seq_len, target_dim)
    tags = torch.ones(batch_size, seq_len).long()
    lengths = torch.tensor([[20] * batch_size]).view(-1) # pylint: disable=not-callable

    decode_input = torch.rand(batch_size, seq_len, len(tag_to_ix))
    score, pred = model._viterbi_decode(decode_input) # pylint: disable=protected-access
    score_b, pred_b = model._viterbi_decode_batch(decode_input) # pylint: disable=protected-access
    score = score.cpu().detach().numpy()
    score_b = score_b.cpu().detach().numpy()
    assert score.shape == score_b.shape
    assert np.sum(score - score_b) < 1e-6
    assert pred.shape == pred_b.shape
    assert np.sum(pred - pred_b) < 1e-6

    # masks = sequence_mask(lengths, seq_len)
    ret = model._forward_alg(feats, lengths) # pylint: disable=protected-access
    retb = model._forward_alg_batch(feats, lengths) # pylint: disable=protected-access
    assert same(ret.cpu().detach().numpy(), retb.cpu().detach().numpy())

    ret = model._score_sentence(feats, tags, lengths) # pylint: disable=protected-access
    retb = model._score_sentence_batch(feats, tags, lengths) # pylint: disable=protected-access
    assert same(ret.cpu().detach().numpy(), retb.cpu().detach().numpy())

if __name__ == '__main__':
    test_model()
