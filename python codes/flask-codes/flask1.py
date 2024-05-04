from flask import Flask 

app = Flask(__name__)

#decorater?!
#OOP,class,git(film)
@app.route("/")   
def index():
    return " In the name of GOD . Hello! This is our first back page index :) " 

@app.route("/hello")
def sayHello():
    return "Hello reza! My name is Hossein."

@app.route("/welcome/")

@app.route("/welcome/<int:id>")
def Welcome(id = None):
    
    msg = "The ID is " + str(id)
    if id is None : msg = "ID can not be empty!"
    return msg 