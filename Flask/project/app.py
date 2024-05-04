import os
import test
from flask import Flask, render_template, url_for, request, redirect, abort, make_response

path = os.path.join("uploads")
os.makedirs(path , exist_ok = True)

app = Flask(__name__)

allowed_format = {"txt" , "py" , "html" , "css" , "png" , "jpg"}
def checkFileformat(fileName):
    formatt = fileName.split(".")[-1]
    return "." in fileName and formatt in allowed_format


@app.route("/")
def home():
   if request.cookies.get("user_email"):
      return f"welcome, your email is : {request.cookies['user_email']}"
   else:
      return render_template("form.html")


@app.route("/submit" ,methods=["POST"])
def submitForm():
   try:
      email = request.form["email"]
      # password = request.form["password"]
      
      response = make_response("successful <br><a href = '/'> Home </a>")
      response.set_cookie("user_email", email)
      return response

   except Exception as ex :
      return f"Sorry! Not successful the error was : {ex} "
   


@app.errorhandler(404)
def showError(error):
   return render_template("error_404.html") , 404

@app.route("/submit" , methods = ["POST"])
def showResult():
   email = request.form["email"]
   password = request.form["password"]
   return render_template("result.html" , email=email , password=password)

@app.route("/upload")
def upload():
   return render_template("upload.html")

@app.route("/uploaded" , methods = ["POST"])
def savefile():
   theFile = request.files["file"]
   
   if checkFileformat(theFile.filename) :
      try :
         goal_path = os.path.join(path , theFile.filename)
         theFile.save(goal_path)
         return "your file has been saved successfully!"
      except Exception as e :
         return "There is an error in saving your file!" + "The error is " + e
   else:
      return "Your format is not allowed!"


print(checkFileformat("index.py"))
   
   
   

