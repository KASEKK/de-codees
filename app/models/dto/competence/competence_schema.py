from marshmallow import Schema, fields, validate

class CompetenceSchema(Schema):
    id = fields.Integer(dump_only=True)
    profil_id = fields.Integer(required=True)
    nom = fields.String(required=True)
    type = fields.String(validate=validate.OneOf(["hard", "soft"]))
    niveau = fields.String(validate=validate.OneOf(["débutante", "intermédiaire", "avancée"]))
