from app import app
from app.controllers.competence_suggestion_controller import CompetenceSuggestionController

@app.route("/competences/suggestions", methods=["GET"])
def get_all_suggestions():
    return CompetenceSuggestionController.get_all()
