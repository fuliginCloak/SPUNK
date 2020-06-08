from flask import Flask, render_template 
app = Flask(__name__)

# nav_links = ['The world', 'Community', 'Help', 'Log In/Register']

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/game')
def the_game():
    return render_template('the_game.html')

@app.route('/community')
def the_community():
    return render_template('community.html')