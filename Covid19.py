from flask import request
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model_path = "./Models/COVID_with 97%.h5"
model = load_model(model_path)



def Covid19_api():
    if request.method == "POST":
        gen = request.form.get("Gender")
        
        if gen == "Female":
            gender = 0
        else:
            gender = 1
        
        age = request.form.get("Age_Above_60")
        if age == "Yes":
            age_above_60 = 1
        else:
            age_above_60 = 0
        
        coug = request.form.get("cough")
        if coug == "Yes":
            cough = 1
        else:
            cough = 0

        short_breath = request.form.get("Shortness_of_breath")
        if short_breath == "Yes":
            shortness_of_breath = 1
        else:
            shortness_of_breath = 0

        fev = request.form.get("Fever")
        if fev == "Yes":
            fever = 1
        else:
            fever = 0
        
        sore = request.form.get("Sore_throat")
        if sore == "Yes":
            sore_throat = 1
        else:
            sore_throat = 0
        
        head = request.form.get("Headache")
        if head == "Yes":
            headache = 1
        else:
            headache = 0
        
        test_indication = request.form.get("Test_Indication")
        if test_indication == "Contact with Confirmed":
            contact_confirmed = 1
            abroad = 0
            other = 0
        elif test_indication == "Abroad":
            contact_confirmed = 0
            abroad = 1
            other = 0 
        else:
            contact_confirmed = 0
            abroad = 0
            other = 1

        img_array = image_load()
        features = [cough,fever,sore_throat,shortness_of_breath,headache,age_above_60,gender,abroad,contact_confirmed,other]         
        features = np.asarray(features,dtype = int)
        features = features.reshape(1,10)
        prediction = model.predict([img_array,features])
        if prediction[0][0] >0.5:
            return "Unfortunately you are Covid Positive"
        else:
            return "Congratulations you are Covid Negative"
        



def image_load():
    
    image_file = request.files["image"]
    image_path = "./images/"+image_file.filename
    image_file.save(image_path)
    img = image.load_img(image_path,target_size=(128,128,3))
    img = np.array(img)
    img = img/255.0
    img = np.expand_dims(img,axis =0)
    return img