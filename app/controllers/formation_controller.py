from app import db
from app.models.db.db_model import Formation
from app.models.dto.formation.formation_schema import FormationSchema

def get_formations_by_profil(profil_id):
    formations = Formation.query.filter_by(profil_id=profil_id).all()
    return FormationSchema(many=True).dump(formations), 200

def create_formation(data):
    formation = Formation(
        profil_id=data.get("profil_id"),
        nom=data.get("nom"),
        organisme=data.get("organisme"),
        date_debut=data.get("date_debut"),
        date_fin=data.get("date_fin"),
        format=data.get("format"),
        type=data.get("type")
    )
    db.session.add(formation)
    db.session.commit()
    return FormationSchema().dump(formation), 201

def update_formation(formation_id, data):
    formation = Formation.query.get(formation_id)
    if not formation:
        return {"message": "Formation non trouvée"}, 404

    for key, value in data.items():
        setattr(formation, key, value)
    db.session.commit()
    return FormationSchema().dump(formation), 200

def delete_formation(formation_id):
    formation = Formation.query.get(formation_id)
    if not formation:
        return {"message": "Formation non trouvée"}, 404

    db.session.delete(formation)
    db.session.commit()
    return {"message": "Formation supprimée avec succès"}, 200

