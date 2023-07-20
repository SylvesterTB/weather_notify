from flask import Flask
from data import *
import logging

logging.basicConfig(filename='logging_info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

app = Flask(__name__)

@app.route('/')
def index():
    return "The web app is working"

@app.route('/start')
def index():
   logging.info('test')
   weather_detector() 

app.run(host='0.0.0.0', port=81)