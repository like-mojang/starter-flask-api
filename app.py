from flask import Flask
import os,botpy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'
