from flask import request
from app import app
from app.controllers import tag_controller

@app.route('/tags', methods=['GET'])
def get_tags():
    return tag_controller.get_all_tags()

@app.route('/tags', methods=['POST'])
def post_tag():
    data = request.get_json()
    return tag_controller.create_tag(data)

@app.route('/users/<int:user_id>/tags', methods=['POST'])
def post_tags_to_user(user_id):
    data = request.get_json()
    tag_ids = data.get('tag_ids', [])
    return tag_controller.add_tags_to_user(user_id, tag_ids)

@app.route('/users/<int:user_id>/tags', methods=['GET'])
def get_user_tags(user_id):
    return tag_controller.get_tags_by_user(user_id)
