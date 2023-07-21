from flask import Flask
from data import *
import logging
from threading import Thread

logging.basicConfig(filename='logging_info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
logging.getLogger().addHandler(logging.StreamHandler())

app = Flask(__name__)

@app.route('/')
def index():
    return "The web app is working"

@app.route('/start')
def weather_start():
    global thread
    if thread is None or not thread.is_alive():
        turn_on()
        thread = Thread(target=weather_detector)
        thread.start()
        return 'Process started', 200
    else:
        return 'Process is already running', 200

@app.route('/stop')
def weather_stop():
    turn_off()
    return 'Process stopped', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, threaded=True)