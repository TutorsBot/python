from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/user/<string:name>')
def userPage(name):
    return render_template('renderht.html', 
                           name = name, 
                           para = "Sample text goes here")
    
if __name__ == "__main__":
    app.debug = True
    app()
    