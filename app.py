from flask import Flask
from requests import get
app = Flask(__name__)

@app.route("/")
def  home():
    response = get('http://127.0.0.1:5000/users').content
    return response

@app.route("/test")
def test():
    return "This is test"


