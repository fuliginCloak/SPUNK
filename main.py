from flask import Flask, render_template, flash, redirect, url_for
from forms import RegisterForm, LoginForm




app = Flask(__name__)


app.config['SECRET_KEY'] = 'a2e52d0421baa64c2243c839243968a2'

@app.route('/')
def home():
    return render_template('landing.html')


# Community/about game header links
@app.route('/aboutgame')
def about_game_links():
    return render_template('about_game_links.html')

@app.route('/community')
def community_links():
    return render_template('community_links.html')


# Login/register header links
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error=None

    if form.username.data == 'admin_spunk.com' and form.password.data == 'password':
        flash(f'Login successful.')
        return redirect (url_for('home'))
    else:
        error = "Invalid username or password"
        flash (error)
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm() 
    if form.validate_on_submit():
        flash(f'Account created, please check your email for confirmation.')
        return redirect (url_for('home'))
    return render_template('register.html', title='Make an account', form=form)
