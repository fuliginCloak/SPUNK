from flask import Flask, render_template 
app = Flask(__name__)

# nav_links = ['The world', 'Community', 'Help', 'Log In/Register']
slogan="A   M o d e r n   M U D"


@app.route('/')
def home():
    return render_template('landing.html',slogan=slogan)

@app.route('/game')
def the_game():
    return render_template('the_game.html')

@app.route('/community')
def the_community():
    return render_template('community.html')

