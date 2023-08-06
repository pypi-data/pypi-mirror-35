'''
Module to manage persistable creation for cross validated techniques (like KFold)

Generally when cross validating, multiple independent persistable need to be
created and then averaged out over.
'''

__author__ = 'Elisha Yadgaran'


class KFoldPersistableCreator(object):
    '''
    Create K instances of objects and custom metric evaluated over all their
    folds
    '''
    pass
