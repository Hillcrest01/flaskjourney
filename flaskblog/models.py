#we create a class for our database and then define the columns that will be there in our database.
#db.Model means that we are inheriting from it and it is a class.
from flaskblog import db

class Item(db.Model):
    #we create the name column
    #in our name column, we are passing db.string because we are expecting strings from the users, then we pass the maximum amount of characters that should be added there and that is 30 to restrict the users from using many and unlimiteed amount of characters.
    #Nullable is set to false to show that we cannot accept null as the name, also, unique is set to true to ensure that all data in our name column are unique to avoid data redundancy.
    #We repeat the same for the remaining columns to ensure we receive data that are precise.

    #id is set as the primary key as it will be used to uniquely identify our data in the database and is also assigned by the database. Always i order of a given criteria.
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False, unique = True)
    #In price, it is an integer so no need to pass the unique argument and also there is no need of setting the maximum length as it will be of no use.
    price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(length = 1000), nullable = False, unique = True)

    def __repr__(self):
        return f'Item{self.name}'

    #after setting your database and writing all the above codes, it is now time to go to the cmd to add the database. 
    #write python to move to the python shell
    # write from <filename> import db
    # with app.appcontext():
    #,indentation> db.create-all()
    #that will create the database and from your vs code you will see <filename.db>

#this is how we add data into our database using cmd
    #>>> from flaskblog import Item
#>>> item1 = Item(name = "Redmi 10A" , price = 100 , description = "desc")
    
#to add and save the data use the following commands for that purpose.
    # with app.appcontext():
    #   db.session.add(item1)
    #   db.session.commit()
    #The column assigned to be the primary key is not assigned a value because it will be automatically assigned to it when the data is added to the database.


    #in order to accesss the stored data, we use the following commands for that
    #>>>
#>>> from flaskblog import Item
#>>> with app.app_context():
#...     Item.query.all()
#...
#[ItemRedmi 10A]
#>>> with app.app_context():
#...     for item in Item.query.all():
#...             item.name
#...             item.price
#...             item.description
#...
#'Redmi 10A'
#100
#'desc'
#>>>
    # isinstance()