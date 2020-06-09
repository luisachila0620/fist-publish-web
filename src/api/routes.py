"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
#from models import Person

api = Blueprint('api', __name__)

todos = ["hello","world"]
@api.route('/todos', methods=['GET'])
def get_todos():

        return jsonify(todos)

@api.route('/todos', methods=['post'])
def post_todos():
    global todos
    payload = request.json
    todos.append(payload)

    return jsonify(payload)


@api.route('/todos/int:position>', methods=['delete'])
def delete_todos(position):
    todos.pop(position)

    return jsonify(todos), 200