import telebot
import requests
from secrets import token, open_weather, acuu_weather
import requests


def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        print(f'Weather in {city}:')
        print(f'Description: {weather_description}')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
    else:
        print('Error fetching data')

# Ваш API ключ
api_key = open_weather

# Назва міста для отримання погоди
city = 'Kyiv'

# Виклик функції для отримання погоди
get_weather(city, api_key)
