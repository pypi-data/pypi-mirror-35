from simpleml.models.base_model import BaseModel

__author__ = 'Elisha Yadgaran'


class BaseClusterer(BaseModel):
    def transform(self, X, y=None, **kwargs):
        '''
        Pass through method to external model
        '''
        return self.external_model.transform(X, y, **kwargs)

    def fit_transform(self, X, y=None, **kwargs):
        '''
        Pass through method to external model
        '''
        return self.external_model.fit_transform(X, y, **kwargs)
