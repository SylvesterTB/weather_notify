from flask import Flask
from data import *


app = Flask(__name__)

@app.route('/')
def index():
   weather_detector() 

app.run(host='0.0.0.0', port=81)