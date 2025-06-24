from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6))
    nom = fields.String()
    prenom = fields.String()
    role = fields.String(validate=validate.OneOf(["admin", "contributrice", "visiteuse"]))
