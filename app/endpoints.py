# app/api/endpoints.py
from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a GET request response"})

@api.route('/data', methods=['POST'])
def post_data():
    payload = request.json
    return jsonify({"message": "You triggered a POST request", "data": payload}), 201
