from flask import Flask, render_template, request, redirect,url_for,session
from flask_restful import Resource, Api, reqparse


app = Flask(__name__,template_folder="templateFiles",static_folder="staticFiles")
api = Api(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/updateimgfile",methods=['POST','GET'])
def createfilerx():
    admincode = request.form["admincode"]
    filename = request.form["filename"]
    filedata = request.form["filedata"]
    
    if(admincode=="1iloveJesus."):

        hedgefile = open(str("{}.jpg".format(filename)),"w")
        hedgefile.write(filedata)
        hedgefile.close()
        return "Done"
    
@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/panel")
def panel():
    return render_template("panel.html",userdata="HEXEBA HOME",userpass="1iloveJesus")


