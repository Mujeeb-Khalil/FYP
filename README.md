# Virtual Consultant

## Introduction
Virtual Consultant is an AI-based web app that will help patients to predict if they have COVID-19 or heart disease with the help of machine learning and deep learning algorithms.

This Project is divided into 3 major segments :

    1. Data Collection & Pre-processing  
    2. Model Training & Testing  
    3. Deployment


## 1. Data Collection & Pre-processing
### 1.1 Heart Disease
We have gathered dataset from [GitHub](https://github.com/sid321axn/Heart-Disease-Prediction-Using-Machine-Learning-Ensemble/blob/master/heart_statlog_cleveland_hungary_final.csv) that contains the medical record of 1190 patients. After collecting the dataset, we have pre-processed it (outlier detection & removal, Handling null values and data normalization). The dataset is divided into two parts training and testing. Training and testing data contain 755 and 189 records respectively.

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
| 40 | Male | Atypical Angina | 140 | 289 | <120 mg/dl | Normal | 172 | 0 | 0.0 | Upsloping | No |

### 1.2 COVID-19
