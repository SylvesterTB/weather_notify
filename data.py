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



#temp_alert = input('At what temperature would you like to be alerted (in celcius)?')
#temp_alert = int(temp_alert)

def weather_detector():
    city = "Munich" 

    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    message_frequency = 60 # in seconds
    temperature_threshhold = 10

    while temperature >= temperature_threshhold:
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["current"]["temp_c"]

        if temperature >= temperature_threshhold:
            telebot('the temperature is greater than', temperature_threshhold)
        else:
            print("")
        time.sleep(message_frequency)

