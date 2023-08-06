'''
Module for vectorizers
'''

from simpleml.transformers.base_transformer import BaseTransformer
from sklearn.feature_extraction import DictVectorizer

__author__ = 'Elisha Yadgaran'


class SklearnDictVectorizer(DictVectorizer, BaseTransformer):
    def transform(self, X, *args, **kwargs):
        '''
        Dict Vectorizer only takes one parameter in
        '''
        return super(SklearnDictVectorizer, self).transform(X)
        
    def get_params(self, *args, **kwargs):
        '''
        Dict Vectorizer returns `dtype` parameter that cannot be
        json serialized. Overwrite to str for now
        '''
        params = super(SklearnDictVectorizer, self).get_params(*args, **kwargs)
        params['dtype'] = str(params['dtype'])

        return params

    def get_feature_names(self, input_feature_names):
        return super(SklearnDictVectorizer, self).get_feature_names()
