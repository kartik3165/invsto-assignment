import unittest
import pandas as pd 
from datetime import datetime

class TestdataValidation(unittest.TestCase):

    def setUp(self):
        self.sample_data = pd.DataFrame ({
            'datetime' : ['2025-01-01 10:00:00' , '2025-01-01 11:00:00'],
            'instrument' : ['AAPL' , 'AAPL'],
            'open' : [150.0 , 152.5],
            'high' : [155.0 ,157.0],
            'low' : [148.5 , 150.0],
            'close' : [154.0 , 156.0],
            'volume' : [1000 , 1200],
        })

    def test_datetime(self):
        self.sample_data['datetime'] = pd.to_datetime(self.sample_data['datetime'])
        self.assertFalse(self.sample_data['datetime'].isnull().any())

    def test_instrument(self):
        for value in self.sample_data['instrument']:
            self.assertTrue(
                type(value) == str
            )

    def test_numericData(self):
        for col in ['open' , 'high' , 'low' , 'close']:
            self.assertTrue(
                pd.api.types.is_numeric_dtype(self.sample_data[col])
            )

    def test_volume(self):
        self.assertTrue(
            pd.api.types.is_integer_dtype(self.sample_data['volume'])
            )
        
if __name__ == '__main__':
    unittest.main()
    
