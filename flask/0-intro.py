from flask import Flask
# import flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/home")
def home():
    return "<em>Home Page</em>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"