from flask import Flask, render_template

# FILTERS !!!!!
# capitalize
# lower
# upper
# title
# trim
# striptags







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

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500    


