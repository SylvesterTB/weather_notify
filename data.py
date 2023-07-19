import requests
from notify_bot import *
import time

import configparser

def read_api_key():
    config = configparser.ConfigParser()

    config.read('config.ini')

    api_key = config.get('Credentials', 'API_KEY')

    return api_key

api_key = read_api_key()



temp_alert = input('At what temperature would you like to be alerted (in celcius)?')
temp_alert = int(temp_alert)
city = "Munich" 

base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(base_url)
data = response.json()

if response.status_code == 200:
    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    weather_description = data["current"]["condition"]["text"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description}")
else:
    print("Error occurred while retrieving weather data.")

while temperature >= temp_alert:
    if temperature >= temp_alert:
        telebot('the temperature is greater than', temp_alert)
    else:
        print("")
    time.sleep(1000)

