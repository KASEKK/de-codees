from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db.db_model import Competence
from app.models.dto.competence.competence_schema import CompetenceSchema
from app.tools.session_scope import session_scope

class CompetenceController(Resource):

    @staticmethod
    def get_all():
        with session_scope() as session:
            competences = session.query(Competence).all()
            schema = CompetenceSchema(many=True)
            result = schema.dump(competences)
            return jsonify(result), 200

    @staticmethod
    def get(competence_id):
        with session_scope() as session:
            competence = session.query(Competence).get(competence_id)
            if not competence:
                return {"message": "Compétence non trouvée"}, 404
            schema = CompetenceSchema()
            result = schema.dump(competence)
            return jsonify(result), 200

    @staticmethod
    def post():
        try:
            data = request.get_json()
            schema = CompetenceSchema()
            competence_data = schema.load(data)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        with session_scope() as session:
            competence = Competence(**competence_data)
            session.add(competence)
            session.commit()
            return schema.dump(competence), 201

    @staticmethod
    def patch(competence_id):
        with session_scope() as session:
            competence = session.query(Competence).get(competence_id)
            if not competence:
                return {"message": "Compétence non trouvée"}, 404

            data = request.get_json()
            for key, value in data.items():
                setattr(competence, key, value)

            session.commit()
            return CompetenceSchema().dump(competence), 200

    @staticmethod
    def delete(competence_id):
        with session_scope() as session:
            competence = session.query(Competence).get(competence_id)
            if not competence:
                return {"message": "Compétence non trouvée"}, 404

            session.delete(competence)
            session.commit()
            return {"message": "Compétence supprimée"}, 200
