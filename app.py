from flask import Flask
from requests import get
app = Flask(__name__)

@app.route("/")
def  home():
    #response = #get('http://127.0.0.1:5000/users').content #api repsone from other flask program
    return 'response' #commented out for now

@app.route("/chalange2")
def htmlDiv():
    return '<h1>THIS IS H!</hv>'

@app.route("/test")
def test():
    return "This is test"


