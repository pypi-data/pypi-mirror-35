'''
Module for transformers that alter dimensionality through feature selection
'''

from simpleml.transformers.base_transformer import BaseTransformer
from sklearn.feature_selection import VarianceThreshold

from itertools import compress


__author__ = 'Elisha Yadgaran'


class SklearnVarianceThreshold(VarianceThreshold, BaseTransformer):
    def transform(self, X, *args, **kwargs):
        '''
        Variance Threshold only takes one parameter in
        '''
        return super(SklearnVarianceThreshold, self).transform(X)

    def get_feature_names(self, input_feature_names):
        feature_mask = self.get_support()
        return compress(input_feature_names, feature_mask)
