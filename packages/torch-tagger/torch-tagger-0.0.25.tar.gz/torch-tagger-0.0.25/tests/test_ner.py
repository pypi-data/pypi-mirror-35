# -*- coding: utf-8 -*-
"""Test NER"""

import os
import uuid
import pickle
import tempfile

from torch_tagger import Tagger
from torch_tagger.utils import text_reader

def train_ner():
    """Train NER model"""
    x_data, y_data = text_reader('/tmp/train.txt')
    x_val, y_val = text_reader('/tmp/valid.txt')
    tag = Tagger(
        batch_size=128,
        epochs=2000,
        embedding_dim=100,
        hidden_dim=100,
        embedding_dropout_p=0.5,
        optimizer='Adam',
        learning_rate=1e-3,
        learning_rate_decay=0.0,
        weight_decay=1e-5
    )
    print('tag model', tag)

    tag_best_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()) + '.pkl')
    print('tag_best_path', tag_best_path)

    tag.fit(x_data, y_data, x_val, y_val, save_best=tag_best_path)

    with open('/tmp/test_ner_masks.pkl', 'wb') as fobj:
        pickle.dump(tag, fobj)

    tag = None
    tag = pickle.load(open('/tmp/test_ner_masks.pkl', 'rb'))

    score = tag.score(x_data, y_data, verbose=1)
    print('train score', score)
    test_ner(tag_best_path)

def test_ner(model_path='/tmp/test_ner_masks.pkl'):
    """Test NER model"""
    x_data, y_data = text_reader('/tmp/test.txt')
    print('load model', model_path)
    tag = pickle.load(open(model_path, 'rb'))
    score = tag.score(x_data, y_data, verbose=1)
    print('test score', score)

if __name__ == '__main__':
    train_ner()
    # test_ner()
