from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'a2e52d0421baa64c2243c839243968a2'
db = SQLAlchemy(app)

from spunkweb import routes