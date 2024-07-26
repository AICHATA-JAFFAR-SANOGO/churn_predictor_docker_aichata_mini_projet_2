# Fichier app.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Chargement du  modèle et du  scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Définition  du schéma de la requête
class CustomerData(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float

@app.post("/predict")
def predict(data: CustomerData):
    # Conversion des données en tableau numpy
    data_array = np.array([[
        data.gender, data.SeniorCitizen, data.Partner, data.Dependents,
        data.tenure, data.PhoneService, data.MultipleLines, data.InternetService,
        data.OnlineSecurity, data.OnlineBackup, data.DeviceProtection, data.TechSupport,
        data.StreamingTV, data.StreamingMovies, data.Contract, data.PaperlessBilling,
        data.PaymentMethod, data.MonthlyCharges, data.TotalCharges
    ]])
    
    # Application  du scaler
    data_scaled = scaler.transform(data_array)
    
    # Prédiction
    prediction = model.predict(data_scaled)
    
    return {"Churn": "Yes" if prediction[0] == 1 else "No"}
