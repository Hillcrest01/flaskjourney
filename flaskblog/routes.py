from flaskblog import app
from flask import render_template
from flaskblog.models import Item

@app.route("/")
@app.route("/home")


def home_page():
    return render_template('home.html')


#In order to navigate to another page, we use the @app.route and specify the name of the other page we want to navigate to.
@app.route("/about")

def about_page():

    return render_template('about.html')

@app.route('/market')

def market_page():
    items = Item.query.all() 
    return render_template('market.html', items=items)

@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)