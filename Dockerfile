# Utilisation d' une image de base officielle de Python
FROM python:3.9-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers requirements.txt et installation des dépendances
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tout le contenu de l'application
COPY . .

# Exposition du port sur lequel l'application va s'exécuter
EXPOSE 8000

# Démarrage de l'application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
