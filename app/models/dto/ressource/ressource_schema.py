from marshmallow import Schema, fields

class RessourceSchema(Schema):
    id = fields.Integer(dump_only=True)
    profil_id = fields.Integer(required=True)
    type = fields.String()
    titre = fields.String()
    url = fields.String()
    commentaire = fields.String()
