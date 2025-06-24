from marshmallow import Schema, fields

class TemoignageSchema(Schema):
    id = fields.Integer(dump_only=True)
    profil_id = fields.Integer(required=True)
    contenu = fields.String(required=True)
    publier = fields.Boolean()
