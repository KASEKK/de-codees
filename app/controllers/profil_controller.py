from app.models.db.db_model import Profil
from app import db

def get_all_profils():
    return Profil.query.all()

def create_profil(data):
    nouveau_profil = Profil(
        user_id=data.get('user_id'),
        biographie=data.get('biographie'),
        motivations=data.get('motivations'),
        annee_reconversion=data.get('annee_reconversion'),
        region=data.get('region')
    )
    db.session.add(nouveau_profil)
    db.session.commit()
    return nouveau_profil

# Récupérer un seul profil
def get_profil_by_id(profil_id):
    return Profil.query.get(profil_id)

# Modifier un profil (partiellement)
def update_profil(profil_id, data):
    profil = Profil.query.get(profil_id)
    if not profil:
        return None

    for key, value in data.items():
        setattr(profil, key, value)

    db.session.commit()
    return profil

# Supprimer un profil
def delete_profil(profil_id):
    profil = Profil.query.get(profil_id)
    if not profil:
        return None

    db.session.delete(profil)
    db.session.commit()
    return profil
