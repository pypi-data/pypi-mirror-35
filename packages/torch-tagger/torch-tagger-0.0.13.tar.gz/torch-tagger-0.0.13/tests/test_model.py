
# -*- coding: utf-8 -*-

import torch
import numpy as np
from torch_tagger.rnn_crf import RNN_CRF
from torch_tagger.utils import sequence_mask

def same(a, b):
    return np.abs(np.sum(np.sum(a - b))) < 1e-6

def test_model():

    device = torch.device('cpu')
    vocab_size = 10
    tag_to_ix = {'<START>': 0, '<STOP>': 1}
    embedding_dim = 10
    hidden_dim = 10

    try:
        model = RNN_CRF(
            vocab_size,
            tag_to_ix,
            embedding_dim,
            hidden_dim,
            device=device,
            rnn_type='unk'
        )
    except Exception as e:
        assert str(e) == 'Invalid rnn_type'


    model = RNN_CRF(
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
    lengths = torch.tensor([[20] * batch_size]).view(-1)
    masks = sequence_mask(lengths, seq_len)

    r = model._forward_alg(feats, lengths)
    rb = model._forward_alg_batch(feats, lengths, masks)
    assert same(r.cpu().detach().numpy(), rb.cpu().detach().numpy())

    r = model._score_sentence(feats, tags, lengths)
    rb = model._score_sentence_batch(feats, tags, lengths, masks)
    assert same(r.cpu().detach().numpy(), rb.cpu().detach().numpy())

if __name__ == '__main__':
    test_model()