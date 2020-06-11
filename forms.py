
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, EqualTo, Length, Email 





class RegisterForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField ('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])

    submit = SubmitField('Make an account')



class LoginForm(FlaskForm):

    username = StringField ('username', validators=[DataRequired()])

    password = PasswordField('Password', validators= [DataRequired()])

    save = BooleanField('Save username?')
    submit = SubmitField('Login')


