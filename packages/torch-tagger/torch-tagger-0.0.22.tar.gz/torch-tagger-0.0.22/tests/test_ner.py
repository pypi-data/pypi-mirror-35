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
        batch_size=128, epochs=50, embedding_dim=100, hidden_dim=100,
        embedding_dropout_p=0.5
    )
    tag.fit(x_data, y_data)

    with open('/tmp/test_ner_masks.pkl', 'wb') as fobj:
        pickle.dump(tag, fobj)

    tag = None
    tag = pickle.load(open('/tmp/test_ner_masks.pkl', 'rb'))

    pred = tag.predict(x_data[:32])
    print('truth')
    print(y_data[0])
    print('predict')
    print(pred[0])
    # assert str(y_data[0]) == str(pred[0]), 'predict should equal to training data'

def test_ner():
    """Test NER model"""
    x_data, y_data = text_reader('/tmp/test.txt')
    tag = pickle.load(open('/tmp/test_ner_masks.pkl', 'rb'))

    score = tag.score(x_data, y_data, verbose=1)
    print('score', score)
    pred = tag.predict(x_data[:32])
    print('truth')
    print(y_data[0])
    print('predict')
    print(pred[0])
    # assert str(y_data[0]) == str(pred[0]), 'predict should equal to training data'

if __name__ == '__main__':
    train_ner()
    test_ner()
