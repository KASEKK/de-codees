from flask import request
from app import app
from app.controllers import ressource_controller

@app.route('/ressources/<int:profil_id>', methods=['GET'])
def get_ressources(profil_id):
    return ressource_controller.get_ressources_by_profil(profil_id)

@app.route('/ressources', methods=['POST'])
def post_ressource():
    data = request.get_json()
    return ressource_controller.create_ressource(data)

@app.route('/ressources/<int:ressource_id>', methods=['PATCH'])
def patch_ressource(ressource_id):
    data = request.get_json()
    return ressource_controller.update_ressource(ressource_id, data)

@app.route('/ressources/<int:ressource_id>', methods=['DELETE'])
def delete_ressource(ressource_id):
    return ressource_controller.delete_ressource(ressource_id)
