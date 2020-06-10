from flask import Flask, render_template 
from forms import RegisterForm, LoginForm



app = Flask(__name__)

# nav_links = ['The world', 'Community', 'Help', 'Log In/Register']
slogan="A   M o d e r n   M U D"

app.config['SECRET_KEY'] = 'a2e52d0421baa64c2243c839243968a2'

@app.route('/')
def home():
    return render_template('landing.html',slogan=slogan)


# Community/about game header links
@app.route('/aboutgame')
def about_game_links():
    return render_template('about_game_links.html')

@app.route('/community')
def community_links():
    return render_template('community_links.html')


# Login/register header links
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title='Make an account', form=form)
