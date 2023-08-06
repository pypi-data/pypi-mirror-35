import unittest
import numpy as np
import pandas as pd
from simpleml.datasets.base_dataset import BaseDataset


class TestableDataset(BaseDataset):
    def build_dataframe(self):
        raise 'Dont use me!'

class DatasetTests(unittest.TestCase):
    def test_hash_consistency(self):
        '''
        Ensure hash equivalence as long as underlying dataset
        hasnt changed
        '''
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df_shuffled = df.sample(frac=1)

        dataset1 = TestableDataset()
        dataset1._dataframe = df

        dataset2 = TestableDataset()
        dataset2._dataframe = df_shuffled

        self.assertEqual(dataset1._hash(), dataset2._hash())

    def test_dataframe_persistence(self):
        '''
        Tests that sql representation of data is equivalent
        to DataFrame
        '''
        dataset2 = QueryableRawDataset.where(
            name=dataset.name,
            registered_name=dataset.registered_name,
            version=dataset.version
        ).first()

        dataset2.load()

        import ipdb; ipdb.set_trace()
        assert(dataset2.dataframe.equals(
            dataset.dataframe.where((pd.notnull(dataset.dataframe)), None).reset_index(drop=True)
        ))
