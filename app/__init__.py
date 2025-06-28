from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import create_engine
from app.config import Config
from sqlalchemy.exc import SQLAlchemyError
from app.config import Config 

from app.models.db.db_model import Base

# Initialisation de l'application Flask
app = Flask(__name__)

# Chargement de la config correctement
app.config.from_object(Config)


csrf = CSRFProtect(app)

# Variable pour vérifier la connexion a à la base de donnée
db_connected = False

# Essayer de se connecter à la base de donnée
try:
    # Initialisation de SQLAclhemy avec l'application flask
    db = SQLAlchemy(app)
    
    engine = create_engine(Config.URL_DB)
    
    # Récupération des métadonnée de la base de donnée à partir du modèle de donnée base
    metadata = Base.metadata
    
    db_connected = True
except SQLAlchemyError as e : 
    # En cas d'erreur SQLAlchemy, affiche un message d'erreur
    print(f"Erreur de connexion à la base de donnée : \n {e}")


if db_connected:
    # Permet de supprimer / recréer la base de donnée
    # metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)
    
    print('------------------------')
    print('Connexion db établie ✅')
    print('------------------------')

    from app.routes import competence_suggestion, competence, temoignage
    from app.routes import ressource, formation, profil, user
    from app.routes import tag
