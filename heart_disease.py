from flask import Flask,render_template,request,url_for
import pickle
import sklearn
import numpy as np
import pandas as pd


filename = "Models/rf_with_96.82% test.pkl"
with open(filename, 'rb') as file:
    model = pickle.load(file)


def heart_disease_api():
    if request.method == "POST":
        age = request.form.get("Age")
        gen = request.form.get("Gender")
        if gen == "Female":
            gender = 0
        else:
            gender = 1
        resting_bp = request.form.get("Resting_bp")
        cholesterol = request.form.get("cholesterol")
        fst = request.form.get("Fasting_blood_sugar")
        if fst == "<120 mg/dl":
            Fasting_blood_sugar = 0
        else:
            Fasting_blood_sugar = 1
        max_heart_rate = request.form.get("heart_rate")
        ea = request.form.get("exercise_angina")
        if ea == "Depicting":
            exercise_angina = 1
        else:
            exercise_angina = 0
        
        oldpeak = request.form.get("oldpeak")
        cp = request.form.get("Chest_Pain_Type")
        if cp == "Typical Angina":
            typ_ang = 1
            atyp_ang = 0
            non_ang = 0
            asympt = 0
        elif cp == "Atypical Angina":
            typ_ang = 0
            atyp_ang = 1
            non_ang = 0
            asympt = 0
        elif cp == "Non Anginal":
            typ_ang = 0
            atyp_ang = 0
            non_ang = 1
            asympt = 0
        else:
            typ_ang = 0
            atyp_ang = 0
            non_ang = 0
            asympt = 1

        slope = request.form.get("ST_slope")
        if slope == "Normal":
            normal_slope = 1
            up_slope = 0
            flat_slope = 0 
            down_slope = 0
        elif slope == "Up sloping":
            normal_slope = 0
            up_slope = 1
            flat_slope = 0 
            down_slope = 0
        elif slope == "Flat":
            normal_slope = 0
            up_slope = 0
            flat_slope = 1
            down_slope = 0
        else:
            normal_slope = 0
            up_slope = 0
            flat_slope = 0 
            down_slope = 1

        ecg = request.form.get("Resting_ecg")
        if ecg == "Normal":
            normal_ecg = 1
            stt_ecg = 0
            left_ecg =0
        elif ecg =="ST-T Wave Abnormality":
            normal_ecg = 0
            stt_ecg = 1
            left_ecg =0
        else:
            normal_ecg = 0
            stt_ecg = 0
            left_ecg =1
        features = [age,gender,resting_bp,cholesterol,Fasting_blood_sugar,max_heart_rate,exercise_angina,oldpeak,asympt,atyp_ang,non_ang,typ_ang,down_slope,flat_slope,normal_slope,up_slope,stt_ecg,left_ecg,normal_ecg]
        features =  np.asarray(features,dtype=float)
        prediction = model.predict([features])
        if prediction[0] == 0:
            pred = "Congratulation you are safe from heart disease"
        else:
            pred = "Unfortunately you have a heart disease"
        return pred
        