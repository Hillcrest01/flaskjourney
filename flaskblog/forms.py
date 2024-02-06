#What we are dealing with here is the creation of a form. And we do this by importing an in-built functio called flask-wtf. 
#Whenever we want to use any functionality or validator, we can just simply import it from wtf.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=5, max=20)])
    
email = StringField('Username', validators=[DataRequired(), Email()])
password = PasswordField('Password', Validators=[DataRequired()])
confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Email()])
    password = PasswordField('Password', Validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
