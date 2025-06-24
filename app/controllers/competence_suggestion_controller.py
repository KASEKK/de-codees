from flask import jsonify
from flask_restful import Resource

from app.models.db.db_model import CompetenceSuggestion
from app.models.dto.competence.competence_suggestion_schema import CompetenceSuggestionSchema
from app.tools.session_scope import session_scope

class CompetenceSuggestionController(Resource):
    def get_all():
        with session_scope() as session:
            suggestions = session.query(CompetenceSuggestion).all()
            schema = CompetenceSuggestionSchema(many=True)
            serialized = schema.dump(suggestions)
        return jsonify(serialized), 200
