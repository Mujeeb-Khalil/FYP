from flask import Flask, render_template 
from heart_disease import heart_disease_api
from Covid19 import Covid19_api


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/HeartDisease")
def heart_disease():
    return render_template("HeartDiseasePredictionform.html")

@app.route("/COVID-19")
def covid_19():
    return render_template("Covid19Predictionform.html")

@app.route("/HeartDisease/Result", methods = ["GET","POST"])
def heart_disease_predict():
    return render_template("heart_disease_result.html", pred = heart_disease_api() )


@app.route("/COVID-19/Result", methods = ["GET","POST"])
def Covid19_predict():
    return render_template("Covid19result.html", pred = Covid19_api())


if __name__ == "__main__":
    app.run(debug = True)