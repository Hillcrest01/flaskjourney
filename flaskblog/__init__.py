#This is the first thing we do when writing flask programs. We import Flask from flask. Notice the casing of the letters in the first and the last flask.


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from forms import RegistrationForm, LoginForm                                                                    

#app is an instance of Flask that defines the routes and runs web applications
#the name shows the name of the current python module and we pass it as an argument
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f98e02651a0ab56894e579e97159e94a'

#we add extra configuration in the app object so that our flask application can recognize its database.
#This is done by adding key values, i.e we create a key SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskblog.db'

#This initializes an instance of SQLAlchemy class allowing us to start using it.
#we pass our application as an argument of the SQLAlchemy class.

db = SQLAlchemy(app)
#we can define a dictionary outside our routes and then access them using render_template.
#This is done by returning render_template in our route functions.

from flaskblog import routes
