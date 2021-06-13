from flask import Flask
from os import environ

config = { 'username': '', 'password': '', 'url': ''  }

config['username'] = environ['CAM_USERNAME']
config['password'] = environ['CAM_PASSWORD']
config['url'] = environ['CAM_URL']

app = Flask(__name__)

import views
