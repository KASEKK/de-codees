from flask_restful import Api
from app.controllers.user_controller import UserController

Api.add_resource(UserController, '/user')
