from marshmallow import Schema, fields, validate

class CompetenceSuggestionSchema(Schema):
    id = fields.Integer(dump_only=True)
    nom = fields.String(required=True)
    type = fields.String(validate=validate.OneOf(["hard", "soft"]))
