import requests
from pprint import pprint

API_Key = '99ea49e87246516b3eee79941f9d89e5'

city = input("Enter the city name: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)