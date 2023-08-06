'''
Module for Converters

Inherently stateless
'''

from simpleml.transformers.base_transformer import BaseTransformer


__author__ = 'Elisha Yadgaran'


class DataframeToRecords(BaseTransformer):
    def transform(self, X, *args, **kwargs):
        return X.to_dict('records')
