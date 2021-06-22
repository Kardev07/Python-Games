import requests
from pprint import pprint

api_key = "fcc6dd07485e26021819a3931539b727"

city = input("Enter a city: ")

baseUrl = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key+"&q="+city

weather_data = requests.get(baseUrl).json()

pprint(weather_data)