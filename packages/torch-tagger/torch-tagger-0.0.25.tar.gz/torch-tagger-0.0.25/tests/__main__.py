# -*- coding: utf-8 -*-
"""Test Entry"""

from tests.test_model import test_model
from tests.test_tagger import test_tagger
from tests.test_grid import test_grid
from tests.test_utils import test_utils

if __name__ == '__main__':
    test_utils()
    test_model()
    test_tagger()
    test_grid()
