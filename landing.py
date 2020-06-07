from flask import Flask, render_template 
app = Flask(__name__)

overview = ['Game', 'Community', 'Help','About', 'Log In']

@app.route('/')
def title():
    return render_template('landing.html', posts=overview)


