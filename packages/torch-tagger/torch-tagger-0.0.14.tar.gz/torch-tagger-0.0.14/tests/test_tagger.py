
# -*- coding: utf-8 -*-

import os
import pickle
import torch
import numpy as np
from torch_tagger import Tagger
from torch_tagger.utils import text_reader

CURRENT = os.path.realpath(os.path.dirname(__file__))
PATH = os.path.join(CURRENT, 'train.txt')
x_data, y_data = text_reader(PATH)

def test_tagger():

    t = Tagger()
    p = t.get_params(True)
    t.set_params(**p)
    t.fit(x_data, y_data)
    with open('/tmp/test_tagger.pkl', 'wb') as fp:
        pickle.dump(t, fp)
    t = pickle.load(open('/tmp/test_tagger.pkl', 'rb'))
    t.predict(x_data)
    t.predict(x_data, verbose=1)
    t.score(x_data, y_data)
    t.score(x_data, y_data, verbose=1)

    for d in ('auto', 'gpu', 'cpu'):
        t = Tagger(device=d)
        try:
            t._get_device()
        except:
            pass

if __name__ == '__main__':
    test_tagger()