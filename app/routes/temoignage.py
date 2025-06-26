from flask import request
from app import app
from app.controllers import temoignage_controller

@app.route('/temoignages/<int:profil_id>', methods=['GET'])
def get_temoignages(profil_id):
    return temoignage_controller.get_temoignages_by_profil(profil_id)

@app.route('/temoignages', methods=['POST'])
def post_temoignage():
    data = request.get_json()
    return temoignage_controller.create_temoignage(data)

@app.route('/temoignages/<int:temoignage_id>', methods=['PATCH'])
def patch_temoignage(temoignage_id):
    data = request.get_json()
    return temoignage_controller.update_temoignage(temoignage_id, data)

@app.route('/temoignages/<int:temoignage_id>', methods=['DELETE'])
def delete_temoignage(temoignage_id):
    return temoignage_controller.delete_temoignage(temoignage_id)
