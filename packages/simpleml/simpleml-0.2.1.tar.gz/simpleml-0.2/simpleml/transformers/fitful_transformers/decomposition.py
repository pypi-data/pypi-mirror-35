'''
Module for transformers that alter dimensionality through decomposition
'''

from simpleml.transformers.base_transformer import BaseTransformer
from sklearn.decomposition import PCA, TruncatedSVD


__author__ = 'Elisha Yadgaran'


class SklearnPCA(PCA, BaseTransformer):
    def transform(self, X, *args, **kwargs):
        '''
        Parent method only takes one input parameter
        '''
        return super(SklearnPCA, self).transform(X)

    def get_feature_names(self, input_feature_names):
        '''
        PCA projects into a new dimension so it isn't possible to easily map
        to original feature names
        '''
        return []


class SklearnTruncatedSVD(TruncatedSVD, BaseTransformer):
    def transform(self, X, *args, **kwargs):
        '''
        Parent method only takes one input parameter
        '''
        return super(SklearnTruncatedSVD, self).transform(X)

    def get_feature_names(self, input_feature_names):
        '''
        SVD projects into a new dimension so it isn't possible to easily map
        to original feature names
        '''
        return []
