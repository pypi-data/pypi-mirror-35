# -*- coding: utf-8 -*-
"""Test NER"""

# import os
import pickle

from torch_tagger import Tagger
from torch_tagger.utils import text_reader

def train_ner():
    """Train NER model"""
    x_data, y_data = text_reader('/tmp/train.txt')
    tag = Tagger(
        batch_size=64,
        epochs=200,
        embedding_dim=100,
        hidden_dim=100,
        embedding_dropout_p=0.5
    )
    print('tag model', tag)
    tag.fit(x_data, y_data)

    with open('/tmp/test_ner_masks.pkl', 'wb') as fobj:
        pickle.dump(tag, fobj)

    tag = None
    tag = pickle.load(open('/tmp/test_ner_masks.pkl', 'rb'))

    score = tag.score(x_data, y_data, verbose=1)
    print('train score', score)
    pred = tag.predict(x_data[:32])
    print('truth')
    print(y_data[0])
    print('predict')
    print(pred[0])

def test_ner():
    """Test NER model"""
    x_data, y_data = text_reader('/tmp/test.txt')
    tag = pickle.load(open('/tmp/test_ner_masks.pkl', 'rb'))

    score = tag.score(x_data, y_data, verbose=1)
    print('test score', score)
    pred = tag.predict(x_data[:32])
    print('truth')
    print(y_data[0])
    print('predict')
    print(pred[0])

if __name__ == '__main__':
    train_ner()
    test_ner()
