import unittest
from weather_service import WeatherService

class TestWeatherService(unittest.TestCase):
    def test_get_weather(self):
        service = WeatherService()
        data = service.get_weather('New York')
        self.assertIn('temperature', data)
        self.assertIn('humidity', data)

    def test_get_weather_cache(self):
        service = WeatherService()
        data1 = service.get_weather('New York')
        data2 = service.get_weather('New York')
        self.assertEqual(data1, data2)  # Ensure data is cached

    def test_handle_api_error(self):
        service = WeatherService()
        data = service.get_weather('InvalidCity')
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()
