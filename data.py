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
def weather_dect():
    city = "Munich" 

    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        weather_description = data["current"]["condition"]["text"]

    

    while temperature >= 20:
        if temperature >= 20:
            telebot('the temperature is greater than', 20)
    else:
        print("")
    time.sleep(1000)

