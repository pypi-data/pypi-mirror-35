'''
Module for Filling Nulls
'''

from simpleml.transformers.base_transformer import BaseTransformer
import pandas as pd

__author__ = 'Elisha Yadgaran'


class FillWithValue(BaseTransformer):
    def __init__(self, values):
        '''
        :param values: either dict or single value, dict fills specified columns (keys)
            with value. Otherwise, whole dataframe gets filled with value
        '''
        self.values = values

    def transform(self, X, *args, **kwargs):
        return X.fillna(self.values)

    def get_params(self, **kwargs):
        return dict(values=self.values)

    def set_params(self, **kwargs):
        self.values = kwargs.get('values', self.values)


# Transformer to fill null with mean
class FillWithMean(BaseTransformer):
    def __init__(self, columns=None):
        self.mean = pd.DataFrame()
        if isinstance(columns, basestring):
            self.columns = [columns]
        else:
            self.columns = columns

    def fit(self, X, y=None, **fit_params):
        if self.columns is None:
            self.mean = X.mean()
        else:
            self.mean = X[self.columns].mean()

        return self

    def transform(self, X, **transform_params):
        if self.columns is None:
            return X.fillna(self.mean)
        else:
            filled_columns = X[self.columns].fillna(self.mean)
            columns_not_to_fill = list(set(X.columns) - set(self.columns))
            untouched_columns = X[columns_not_to_fill]

            return pd.concat([filled_columns, untouched_columns], axis=1)

    def get_params(self, **kwargs):
        return dict(columns=self.columns)


# Transformer to fill null with mode
class FillWithMode(BaseTransformer):
    def __init__(self, columns=None):
        self.mode = pd.DataFrame()
        if isinstance(columns, basestring):
            self.columns = [columns]
        else:
            self.columns = columns

    def fit(self, X, y=None, **fit_params):
        if self.columns is None:
            self.mode = X.mode()
        else:
            self.mode = X[self.columns].mode()

        return self

    def transform(self, X, **transform_params):
        if self.columns is None:
            return X.fillna(self.mode.iloc[0])
        else:
            filled_columns = X[self.columns].fillna(self.mode.iloc[0])
            columns_not_to_fill = list(set(X.columns) - set(self.columns))
            untouched_columns = X[columns_not_to_fill]

            return pd.concat([filled_columns, untouched_columns], axis=1)

    def get_params(self, **kwargs):
        return dict(columns=self.columns)


# class FillWithMedian(BaseTransformer):
