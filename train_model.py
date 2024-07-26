#Fichier train_model.py (c'est mon modèle )

import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Chargement des données prétraitées
X = np.load('X_scaled.npy')
y = np.load('y.npy')

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialisation  et entraînement du  modèle
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Évaluation du  modèle
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Sauvegarde du modèle
joblib.dump(model, 'model.pkl')
