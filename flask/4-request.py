from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('request.html')

@app.route('/login', methods=['GET', 'POST'])
def page():
    if request.method == 'POST':
        print(request.form['username'], request.form['password'])
        return render_template('/dashboard.html',un =request.form['username'], pd = request.form['password'])
    else:
        return render_template('/login.html')
    

