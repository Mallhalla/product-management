from flask import Blueprint, jsonify, request
from app.connect_to_mongo import get_products

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    products = get_products()
    return jsonify(products)

@api.route('/data', methods=['POST'])
def post_data():
    payload = request.json
    return jsonify({"message": "You triggered a POST request", "data": payload}), 201
