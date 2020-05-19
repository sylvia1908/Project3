from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import LoadData

# Create an instance of Flask
app = Flask(__name__)
# Mars ={}

mongo = PyMongo(app, uri="mongodb://localhost:27017/Covid19")

@app.route("/")
def index():
    Covid19 = mongo.db.Covid19
    Covid19_data = LoadData.getData()
    Covid19.update({}, Covid19_data, upsert=True)
    return render_template("index.html")

@app.route("/map")
def map():

    return render_template("map.html")

@app.route("/Californiamap")
def Californiamap():

    return render_template("Californiamap.html")

@app.route("/Incidentrate")
def Incidentrate():

    return render_template("Incidentrate.html")

@app.route("/stateData2")
def stateData2():

    return render_template("stateData2.html")

@app.route("/StatesData")
def StatesData():

    return render_template("StatesData.html")

@app.route("/Form")
def Form():

    return render_template("Form.html")


if __name__ == "__main__":
    app.run(debug=True)
