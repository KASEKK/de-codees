from marshmallow import Schema, fields

class FormationSchema(Schema):
    id = fields.Integer(dump_only=True)
    profil_id = fields.Integer(required=True)
    nom = fields.String(required=True)
    organisme = fields.String()
    date_debut = fields.String()
    date_fin = fields.String()
    format = fields.String()  # en ligne / présentiel
    type = fields.String()    # certif / bootcamp...
