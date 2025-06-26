from app import app
from flask import request
from app.controllers.competence_controller import CompetenceController

# GET ALL
@app.route("/competences", methods=["GET"])
def get_all_competences():
    return CompetenceController.get_all()

# GET ONE
@app.route("/competences/<int:competence_id>", methods=["GET"])
def get_competence(competence_id):
    return CompetenceController.get(competence_id)

# POST
@app.route("/competences", methods=["POST"])
def create_competence():
    return CompetenceController.post()

# PATCH
@app.route("/competences/<int:competence_id>", methods=["PATCH"])
def update_competence(competence_id):
    return CompetenceController.patch(competence_id)

# DELETE
@app.route("/competences/<int:competence_id>", methods=["DELETE"])
def delete_competence(competence_id):
    return CompetenceController.delete(competence_id)
