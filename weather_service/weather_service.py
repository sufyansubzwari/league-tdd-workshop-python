import requests
import time

class WeatherService:
    def __init__(self):
        self.cache = {}
        self.cache_duration = 600  # cache duration in seconds

    def get_weather(self, city):
        current_time = time.time()

        # Check cache first
        if city in self.cache:
            cached_data, timestamp = self.cache[city]
            if current_time - timestamp < self.cache_duration:
                return cached_data

        # Fetch new data
        try:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4523628bd365a0c61f43c9ba0c9cd1ff&units=imperial')
            response.raise_for_status()
            data = response.json()
            weather_data = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity']
            }
            # Update cache
            self.cache[city] = (weather_data, current_time)
            return weather_data
        except requests.RequestException:
            return None
