from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return f'<div>error go to <a href="/">Go to homepage</a></div>'