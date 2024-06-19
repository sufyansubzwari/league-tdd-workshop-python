import unittest
import pandas as pd
from house_price_model import HousePriceModel
from pathlib import Path

data_path = Path(__file__).resolve().parent / 'data.csv'

class TestHousePriceModel(unittest.TestCase):
    def test_data_preprocessing(self):
        model = HousePriceModel()
        data = model.load_data(data_path)
        processed_data = model.preprocess_data(data)
        self.assertIn('price', processed_data.columns)
        self.assertIn('sqft', processed_data.columns)
        self.assertIn('bedrooms', processed_data.columns)
        self.assertIn('bathrooms', processed_data.columns)

    def test_model_training(self):
        model = HousePriceModel()
        data = model.load_data(data_path)
        processed_data = model.preprocess_data(data)
        model.train(processed_data)
        self.assertIsNotNone(model.model)

    def test_model_prediction(self):
        model = HousePriceModel()
        data = model.load_data(data_path)
        processed_data = model.preprocess_data(data)
        model.train(processed_data)
        predictions = model.predict(processed_data)
        self.assertEqual(len(predictions), len(processed_data))

if __name__ == '__main__':
    unittest.main()
