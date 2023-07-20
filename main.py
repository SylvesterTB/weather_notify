from flask import Flask
from data import *
import logging
import schedule

logging.basicConfig(filename='logging_info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

app = Flask(__name__)

@app.route('/')
def index():
   logging.info('test')
   schedule.every(1).minutes.do(weather_detector)

app.run(host='0.0.0.0', port=81)