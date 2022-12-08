from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create a Flask Instance
app = Flask(__name__)

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:easy@localhost/myfirstdb'
# Secret Key!
app.config['SECRET_KEY'] = "R3EWTG BWBE NYTJT JM YEYR "

#Initialize The Database
db = SQLAlchemy(app)


# Create a Model - what do want to save to the database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name

# Create a Form Class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What is your name ?", validators=[DataRequired()])
    submit = SubmitField("Submit")

 # BooleanField
    # DataField
    # DataTimeField
    # DecimalField
    # FileField
    # HiddenField
    # MultipleField
    # FieldList
    # FloatField
    # FormField
    # IntergerField
    # PasswordField
    # RadioField
    # SelectField
    # SelectMultipleField
    # StringField
    # TextAreaField

    ## Validators
    # DataRequired
    # Email
    # EqualTo
    # InputRequired
    # IPAddress
    # MacAddress
    # Length
    # NumberRange
    # Optional
    # Regexp
    # URL
    # UUID
    # AnyOf
    # NoneOf



# FILTERS !!!!!
# capitalize
# lower
# upper
# title
# trim
# striptags




# Create Name Page
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
        return render_template("add_user.html")

#Create a route decorrator
@app.route('/')
def index():
    #return "Hello world"
    #return render_template("index.html")
    fav_car = "BMW"
    cars = ["Ford", "Volvo", "BMW", 20000, 431413]
    return render_template("index.html", the_car=fav_car, brands=cars)


# localhost:5000/user/Kafu
@app.route('/user/<name>')  
def user(name):
    #return "Hello {}".format(name)
    return render_template("user.html", user_name=name)



# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
# Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!!!")
    return render_template("name.html", name = name, form = form)





with app.app_context():
    db.create_all()



# Create Custom Error Pages
 
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500    




if __name__ == '__main__':
    app.run(host='localhost', port=5000)