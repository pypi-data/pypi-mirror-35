"""
Keel yeast4 dataset.

@author: David Diaz Vico
@license: MIT
"""

from ..base import load_imbalanced


def load_yeast4(return_X_y=False):
    """Load yeast4 dataset.

    Loads the yeast4 dataset.

    Parameters
    ----------
    return_X_y: bool, default=False
                If True, returns (data, target) instead of a Bunch object..

    Returns
    -------
    data: Bunch
          Dictionary-like object with all the data and metadata.
    X, y: arrays
          If return_X_y is True

    """
    return load_imbalanced('yeast4',
                           'http://sci2s.ugr.es/keel/keel-dataset/datasets/imbalanced/imb_IRhigherThan9p1',
                           names=['Mcg', 'Gvh', 'Alm', 'Mit', 'Erl', 'Pox',
                                  'Vac', 'Nuc', 'Class'],
                           target_names=['Class'], return_X_y=return_X_y)
