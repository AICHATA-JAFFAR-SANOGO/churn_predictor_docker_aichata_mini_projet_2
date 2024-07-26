#Fichier streamlit_app.py

import streamlit as st
import requests

st.title("Churn Predictor")

# Inputs pour les caractéristiques du client
gender = st.selectbox('Gender', [0, 1])  
SeniorCitizen = st.selectbox('Senior Citizen', [0, 1])
Partner = st.selectbox('Partner', [0, 1])
Dependents = st.selectbox('Dependents', [0, 1])
tenure = st.number_input('Tenure', min_value=0, max_value=72)
PhoneService = st.selectbox('Phone Service', [0, 1])
MultipleLines = st.selectbox('Multiple Lines', [0, 1, 2])  
InternetService = st.selectbox('Internet Service', [0, 1, 2])  
OnlineSecurity = st.selectbox('Online Security', [0, 1])
OnlineBackup = st.selectbox('Online Backup', [0, 1])
DeviceProtection = st.selectbox('Device Protection', [0, 1])
TechSupport = st.selectbox('Tech Support', [0, 1])
StreamingTV = st.selectbox('Streaming TV', [0, 1])
StreamingMovies = st.selectbox('Streaming Movies', [0, 1])
Contract = st.selectbox('Contract', [0, 1, 2])  
PaperlessBilling = st.selectbox('Paperless Billing', [0, 1])
PaymentMethod = st.selectbox('Payment Method', [0, 1, 2, 3])  
MonthlyCharges = st.number_input('Monthly Charges', min_value=0.0)
TotalCharges = st.number_input('Total Charges', min_value=0.0)

# Bouton de prédiction
if st.button('Predict Churn'):
    # Envoyer les données à l'API
    response = requests.post("https://churn-predictor-solution-mini-projet-1.onrender.com/predict", json={
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    })
    
    result = response.json()
    st.write(f"Churn Prediction: {result['Churn']}")
