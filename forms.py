from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators






class RegisterForm(Form):
    username=StringField('Username', [validators.DataRequired(), validators.Length(min=2, max=20)])

    email = StringField ('Email', [validators.DataRequired(), validators.Email()])

    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password')])

    submit = SubmitField('Make an account')



class LoginForm(Form):

    email = StringField ('Email',[validators.DataRequired(), validators.Email()])

    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])

    cookie_remember = BooleanField('Save username?')
    submit = SubmitField('Login')


