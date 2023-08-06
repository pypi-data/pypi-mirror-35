# -*- coding: utf-8 -*-

import os
import pickle
from sklearn.model_selection import GridSearchCV

from torch_tagger import Tagger
from torch_tagger.utils import text_reader

CURRENT = os.path.realpath(os.path.dirname(__file__))
PATH = os.path.join(CURRENT, 'train.txt')
x_data, y_data = text_reader(PATH)

def basic_test():
    tag = Tagger(batch_size=8, epochs=500)
    tag.fit(x_data, y_data)

    with open('/tmp/test.pkl', 'wb') as fp:
        pickle.dump(tag, fp)

    tag = None
    tag = pickle.load(open('/tmp/test.pkl', 'rb'))

    score = tag.score(x_data, y_data)
    print('score', score)
    pred = tag.predict(x_data[:32])
    print('truth')
    print(y_data[0])
    print('predict')
    print(pred[0])
    assert str(y_data[0]) == str(pred[0]), 'predict should equal to training data'

def grid_test():
    parameters = {
        'embedding_dim': (16, 32),
        'hidden_dim': (16, 32),
        'bidirectional': (True, False),
        'rnn_type': ('lstm', 'gru'),
        'num_layers': (1, 2)
    }
    tag = Tagger(batch_size=1, epochs=10, verbose=0)
    clf = GridSearchCV(tag, parameters, verbose=2, n_jobs=1)
    clf.fit(x_data, y_data)
    print(clf.cv_results_['mean_test_score'])
    print(clf.best_estimator_)

if __name__ == '__main__':
    # basic_test()
    grid_test()
