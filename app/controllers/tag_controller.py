from app import db
from app.models.db.db_model import Tag, User, UserTag
from app.models.dto.tag.tag_schema import TagSchema

# GET – tous les tags
def get_all_tags():
    tags = Tag.query.all()
    return TagSchema(many=True).dump(tags), 200

# POST – créer un nouveau tag
def create_tag(data):
    tag = Tag(nom=data.get("nom"))
    db.session.add(tag)
    db.session.commit()
    return TagSchema().dump(tag), 201

# POST – associer des tags à un user
def add_tags_to_user(user_id, tag_ids):
    user = User.query.get(user_id)
    if not user:
        return {"message": "Utilisateur non trouvé"}, 404

    for tag_id in tag_ids:
        if not any(t.id == tag_id for t in user.tags):
            tag = Tag.query.get(tag_id)
            if tag:
                user.tags.append(tag)

    db.session.commit()
    return {"message": "Tags ajoutés avec succès"}, 200

# GET – récupérer les tags d’un user
def get_tags_by_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"message": "Utilisateur non trouvé"}, 404
    return TagSchema(many=True).dump(user.tags), 200
