from flask import request
from app import app
from app.controllers.user_controller import UserController

user_controller = UserController()

@app.route('/user', methods=['POST'])
def create_user():
    return user_controller.post()

@app.route('/user', methods=['GET'])
def get_user_by_email():
    return user_controller.get()

@app.route('/user', methods=['PATCH'])
def update_user():
    return user_controller.patch()

@app.route('/user', methods=['DELETE'])
def delete_user():
    return user_controller.delete()
