from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return 'The temperature in Munich' 

app.run(host='127.0.0.1', port=80)