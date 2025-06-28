# app/controllers/user_controller.py
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash
from app.models.db.db_model import User
from app.models.dto.user.user_schema import UserSchema
from app import db

class UserController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        parser.add_argument('nom', required=True)
        parser.add_argument('prenom', required=True)
        parser.add_argument('role', required=True, choices=('admin', 'contributrice', 'visiteuse'))
        args = parser.parse_args()

        # Vérification si l'utilisateur existe déjà
        if User.query.filter_by(email=args['email']).first():
            return {'message': 'Cet email est déjà utilisé.'}, 400

        # Hash du mot de passe
        hashed_pw = generate_password_hash(args['password'])

        new_user = User(
            email=args['email'],
            password=hashed_pw,
            nom=args['nom'],
            prenom=args['prenom'],
            role=args['role']
        )

        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': f'Erreur lors de la création : {str(e)}'}, 500

        return UserSchema().dump(new_user), 201

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='args', required=True)
        args = parser.parse_args()

        user = db.session.query(User).filter_by(email=args['email']).first()

        if not user:
            return {'message': 'Utilisateur non trouvé.'}, 404

        return UserSchema().dump(user), 200

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)  # Pour identifier l'utilisateur
        parser.add_argument('password')
        parser.add_argument('nom')
        parser.add_argument('prenom')
        parser.add_argument('role')
        args = parser.parse_args()

        user = User.query.filter_by(email=args['email']).first()
        if not user:
            return {'message': 'Utilisateur non trouvé.'}, 404

        if args['password']:
            user.password = generate_password_hash(args['password'])
        if args['nom']:
            user.nom = args['nom']
        if args['prenom']:
            user.prenom = args['prenom']
        if args['role']:
            user.role = args['role']

        db.session.commit()
        return UserSchema().dump(user), 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)
        args = parser.parse_args()

        user = User.query.filter_by(email=args['email']).first()
        if not user:
            return {'message': 'Utilisateur non trouvé.'}, 404

        db.session.delete(user)
        db.session.commit()
        return {'message': 'Utilisateur supprimé avec succès'}, 200

