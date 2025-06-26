from app import db
from app.models.db.db_model import Ressource
from app.models.dto.ressource.ressource_schema import RessourceSchema

# GET – toutes les ressources d’un profil
def get_ressources_by_profil(profil_id):
    ressources = Ressource.query.filter_by(profil_id=profil_id).all()
    return RessourceSchema(many=True).dump(ressources), 200

# POST – créer une ressource
def create_ressource(data):
    ressource = Ressource(
        profil_id=data.get("profil_id"),
        type=data.get("type"),
        impact=data.get("impact"),
        titre=data.get("titre"),
        url=data.get("url"),
        commentaire=data.get("commentaire")
    )
    db.session.add(ressource)
    db.session.commit()
    return RessourceSchema().dump(ressource), 201

# PATCH – modifier une ressource
def update_ressource(ressource_id, data):
    ressource = Ressource.query.get(ressource_id)
    if not ressource:
        return {"message": "Ressource non trouvée"}, 404

    for key, value in data.items():
        setattr(ressource, key, value)
    db.session.commit()
    return RessourceSchema().dump(ressource), 200

# DELETE – supprimer une ressource
def delete_ressource(ressource_id):
    ressource = Ressource.query.get(ressource_id)
    if not ressource:
        return {"message": "Ressource non trouvée"}, 404

    db.session.delete(ressource)
    db.session.commit()
    return {"message": "Ressource supprimée avec succès"}, 200
