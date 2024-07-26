#Fichier  analyze_columns.py

import pandas as pd

# Chargement des données
df = pd.read_csv('churn_predictor.csv')

# Affichage des premières lignes du DataFrame
print("Premières lignes du DataFrame :")
print(df.head())

# Affichage du résumé des colonnes
print("\nRésumé des colonnes :")
print(df.info())

# Affichage des types de données pour chaque colonne
print("\nTypes de données des colonnes :")
print(df.dtypes)

# Affichage des valeurs uniques des colonnes pour identifier les colonnes catégorielles
print("\nValeurs uniques des colonnes :")
for column in df.columns:
    print(f"\nColonne: {column}")
    print(df[column].unique())
