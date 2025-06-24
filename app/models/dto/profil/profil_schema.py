from marshmallow import Schema, fields

class ProfilSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    biographie = fields.String()
    motivations = fields.String()
    annee_reconversion = fields.Integer()
    region = fields.String()
