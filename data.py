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

def get_temperature():
        city = "Munich" 
        base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["current"]["temp_c"]

        return temperature

running = True

def turn_off():
    running = False

def turn_on():
     running = True

def weather_detector():
    message_frequency = 60 # in seconds
    temperature_threshhold = 10
    temperature = get_temperature()
    while running:
        current_time = time.time()
        if temperature >= temperature_threshhold:
            telebot('the temperature is greater than', temperature_threshhold)
        else:
            print("")
        temperature = get_temperature()
        time.sleep(message_frequency)

             