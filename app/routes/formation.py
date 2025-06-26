from flask import request
from app import app
from app.controllers import formation_controller

@app.route('/formations/<int:profil_id>', methods=['GET'])
def get_formations(profil_id):
    return formation_controller.get_formations_by_profil(profil_id)

@app.route('/formations', methods=['POST'])
def post_formation():
    data = request.get_json()
    return formation_controller.create_formation(data)

@app.route('/formations/<int:formation_id>', methods=['PATCH'])
def patch_formation(formation_id):
    data = request.get_json()
    return formation_controller.update_formation(formation_id, data)

@app.route('/formations/<int:formation_id>', methods=['DELETE'])
def delete_formation(formation_id):
    return formation_controller.delete_formation(formation_id)
