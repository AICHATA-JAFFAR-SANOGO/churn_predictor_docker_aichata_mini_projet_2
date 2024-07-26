#Fichier prepare_data.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import numpy as np

# Chargement des données
df = pd.read_csv('churn_predictor.csv')

# Conversion de  TotalCharges en float
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Remplacement  des valeurs manquantes dans TotalCharges par la moyenne de la colonne
df['TotalCharges'].fillna(df['TotalCharges'].mean(), inplace=True)

# Encodage des colonnes catégorielles
categorical_cols = df.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Séparation des caractéristiques et la cible
X = df.drop(['Churn', 'customerID'], axis=1)
y = df['Churn']

# Normalisation des caractéristiques
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Sauvegarde des encoders et des données prétraitées
joblib.dump(label_encoders, 'label_encoders.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Sauvegarder des données prétraitées
np.save('X_scaled.npy', X_scaled)
np.save('y.npy', y.to_numpy())

print("Préparation des données terminée.")
