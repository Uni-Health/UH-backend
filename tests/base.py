import requests, json, pytest
from flask import Flask

SERVER = 'http://127.0.0.1:5000/'

s = requests.Session()