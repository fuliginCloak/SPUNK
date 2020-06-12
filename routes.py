from flask import  render_template, flash, redirect, url_for, \
    request
from spunkweb import app
from spunkweb.forms import RegisterForm, LoginForm
from spunkweb.models import User, Post

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

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'password':
                error = 'username or password invalid!'
                
        else:
            flash(f'Login successful.')
            return redirect (url_for('home'))
         
          
           
    
    return render_template('login.html', title='Login', form=form, error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm() 
    if form.validate_on_submit():
        flash(f'Account created, please check your email for confirmation.')
       
        return redirect (url_for('home'))
    return render_template('register.html', title='Make an account', form=form)
    
