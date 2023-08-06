"""
Tests.

@author: David Diaz Vico
@license: MIT
"""

from ...base import check_load_dataset

from skdatasets.keel.imbalanced import load_yeast5


def test_load_yeast5():
    """Tests yeast5 dataset."""
    n_patterns = (1484, )
    n_variables = 8
    array_names = (('data', 'target'), )
    n_folds = (5, )
    check_load_dataset(load_yeast5, n_patterns, n_variables, array_names,
                       n_targets=None, n_folds=n_folds)
