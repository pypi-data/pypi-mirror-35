import unittest
import numpy as np
import pandas as pd
from simpleml.datasets.base_dataset import BaseDataset


class PipelineTests(unittest.TestCase):
    def test_missing_dataset_persistence_error(self):
        '''
        Assert error is raised if trying to save a pipeline without
        adding a dataset (and fitting) first
        '''

    def test_unfit_persistence_error(self):
        '''
        Assert error is raised if trying to save a pipeline without
        fitting the transformers on the dataset
        '''

    def test_missing_dataset_fit_or_transform_error(self):
        '''
        Assert error is raised if trying to fit or transform a dataset without
        adding a dataset first
        '''

    def test_unfit_transform_error(self):
        '''
        Assert error is raised if trying to transform a pipeline without
        fitting the transformers on the dataset first
        '''

    def test_hash_consistency(self):
        '''
        Ensure hash equivalence as long as underlying data
        hasnt changed
        '''
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df_shuffled = df.sample(frac=1)

        dataset1 = BaseDataset()
        dataset1._dataframe = df

        dataset2 = BaseDataset()
        dataset2._dataframe = df_shuffled

        self.assertEqual(dataset1._hash(), dataset2._hash())

    def test_persistence(self):
        '''
        Assert loaded object is the same as original
        '''
        pipeline = BaseDatasetPipeline()
        pipeline.add_dataset(BaseDataset())
        pipeline.fit()
        pipeline.save()

        pipeline2 = BaseDatasetPipeline.where(
            name=pipeline.name,
            version=pipeline.version
        ).first()

        pipeline2.load()
        assert(pipeline.external_pipeline == pipeline2.external_pipeline)

    def test_dataset_doesnt_load_externals_by_default(self):
        pass

    def test_dataset_loads_externals_when_referenced(self):
        pass


class DatasetPipelineTests(unittest.TestCase):
    pass
