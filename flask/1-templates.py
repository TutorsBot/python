from flask import Flask, render_template
from numpy import true_divide

App = Flask(__name__)

@App.route('/')
def index():
    """
    Display the index page accessible at '/'
    """
    return render_template('index.html')


@App.route('/other')
def other():
    """
    Display other.html which is accessible at '/other'
    """
    return render_template('other.html')

@App.route('/about')
def about():
    """
    Display other.html which is accessible at '/other'
    """
    return render_template('other.html')

if __name__ == '__main__':
    App.debug = True
    App()