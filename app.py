from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World this is home"

@app.route("/test")
def test():
    return "This is test"

@app.route("/Commit1")
def test():
    return "This is commit 1"