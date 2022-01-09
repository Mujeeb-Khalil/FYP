from flask import Flask,render_template,request,url_for
import pickle
import numpy as np
import pandas as pd
from heart_disease import heart_disease_api
from Covid19 import Covid19_api


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/heart_disease")
def heart_disease():
    return render_template("heart_disease.html")

@app.route("/Covid19")
def covid_19():
    return render_template("Covid19.html")


@app.route("/heart_disease/predict_form")
def heart_disease_prediction_form():
    return render_template("HeartDiseasePredictionform.html")

@app.route("/Covid19/predict_form")
def Covid19_prediction_form():
    return render_template("Covid19_Detectionform.html")



@app.route("/heart_disease/predict_form/predict",methods = ["GET","POST"])
def heart_disease_predict():
    return render_template("heart_disease_predict.html",prediction = heart_disease_api())

@app.route("/Covid19/predict_form/predict",methods = ["GET","POST"])
def Covid19_predict():
    return render_template("Covid19_Prediction.html",pred = Covid19_api())

if __name__ == "__main__":
    app.run(debug = True)