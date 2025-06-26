from app import db
from app.models.db.db_model import Temoignage
from app.models.dto.temoignage.temoignage_schema import TemoignageSchema

def get_temoignages_by_profil(profil_id):
    temoignages = Temoignage.query.filter_by(profil_id=profil_id).all()
    return TemoignageSchema(many=True).dump(temoignages), 200

def create_temoignage(data):
    temoignage = Temoignage(
        profil_id=data.get("profil_id"),
        contenu=data.get("contenu"),
        publier=data.get("publier", False)
    )
    db.session.add(temoignage)
    db.session.commit()
    return TemoignageSchema().dump(temoignage), 201

def update_temoignage(temoignage_id, data):
    temoignage = Temoignage.query.get(temoignage_id)
    if not temoignage:
        return {"message": "Témoignage non trouvé"}, 404

    for key, value in data.items():
        setattr(temoignage, key, value)
    db.session.commit()
    return TemoignageSchema().dump(temoignage), 200

def delete_temoignage(temoignage_id):
    temoignage = Temoignage.query.get(temoignage_id)
    if not temoignage:
        return {"message": "Témoignage non trouvé"}, 404

    db.session.delete(temoignage)
    db.session.commit()
    return {"message": "Témoignage supprimé avec succès"}, 200

