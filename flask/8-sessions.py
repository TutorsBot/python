from flask import Flask, make_response, session,redirect,url_for, render_template

app = Flask(__name__)
app.secret_key = 'sample'
@app.route('/login')
def login():
    session['username'] = "fazlur"
    return redirect(url_for('dashboard'))
    
@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    print(username)
    return render_template('dashboard.html', username = username)