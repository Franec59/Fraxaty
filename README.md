# Projet Fraxaty


Installez les dépendances PIP nécessaires au bon fonctionnement de l'application

```bash

py -m pip install -r requirements.txt

```

Créez une fichier `.env` dans la racine du projet et remplissez les variables d'environnement conformément aux informations de connexion de votre base de données. 

```bash

DB_USER=root
DB_PWD=password
DB_HOST=localhost
DB_PORT=3310
DB_NAME=medical
DB_AUTOCOMMIT=1

```

Placez-vous à la racine du projet lancez la commande suivante :

```bash

flask run

```