# Virtual Consultant

## Introduction
Virtual Consultant is an AI-based web app that will help patients to predict if they have COVID-19 or heart disease with the help of machine learning and deep learning algorithms.

This Project is divided into 3 major segments :

    1. Data Collection & Pre-processing  
    2. Model Training & Testing  
    3. Deployment


## 1. Data Collection & Pre-processing
### 1.1 Heart Disease
We have gathered dataset from [GitHub](https://github.com/sid321axn/Heart-Disease-Prediction-Using-Machine-Learning-Ensemble/blob/master/heart_statlog_cleveland_hungary_final.csv) that contains the medical record of 1190 patients. After collecting the dataset, we have pre-processed it (outlier detection & removal, Handling null values and data normalization). The dataset is divided into subsets training and testing. Training and testing data contain 755 and 189 records respectively.

Dataset contain following attributes
- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure 
- Cholesterol 
- Fasting Blood Sugar 
- Resting ECG 
- Max Heart Rate 
- Exercise Angina 
- Old peak 
- ST-Slope


First 5 rows of the dataset
| Age | Gender | Chest Pain Type | Resting Blood Pressure | Cholesterol | Fasting Blood Sugar | Resting ECG | Max Heart Rate | Exercise Angina | Oldpeak | ST Slope | Target |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 40 | Male | Atypical Angina | 140 | 289 | <120 mg/dl | Normal | 172 | 0 | 0.0 | Up sloping | No |
| 49 | Female | Non-Anginal Pain | 160 | 180 | <120 mg/dl | Normal | 156 | 0 | 1.0 | Flat | Yes |
| 37 | Male | Atypical Angina | 130 | 283 | <120 mg/dl | ST-T Wave Abnormality | 98 | 0 | 0.0 | Up sloping | No |
| 48 | Female | Asymptomatic | 138 | 214 | <120 mg/dl | Normal | 108 | 1 | 1.5 | Flat | Yes |
| 54 | Male | Non-Anginal Pain | 150 | 195 | <120 mg/dl | Normal | 122 | 0 | 0.0 | Up sloping | No |
### 1.2 COVID-19

## 2. Model Training & Testing
### 2.1 Heart Disease Prediction
We have used different machine learning and deep learning algorithms such as Random Forest Classifier, Extreme Gradient Boosting, Logistic Regression, Artificial Neural Network and Convolutional Neural Network.

### 2.2 COVID-19 Prediction

For COVID-19 Prediction, we have used Multi-Input Modal that takes the X-ray image and COVID-19 Symptoms as input and return the prediction. We have used Convolutional Neural Network and ResNet50 for COVID-19 Prediction.

## 3. Deployment
We have used HTML, CSS, Javascript, and bootstrap to design and develop the frontend of the webpage. Python's framework flask is used to develop the backend of the webapp. We have deployed the website on Heroku.





## Languages and Frameworks
- HTML
- CSS
- Javascript
- Bootstrap
- Python
- Numpy
- Pandas
- Tensorflow
- Keras
- Flask
- Scikit-Learn
- Pillow