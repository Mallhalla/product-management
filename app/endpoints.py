from flask import Blueprint, jsonify, request
from app.product_service import get_all_products

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    products = get_all_products()
    return jsonify(products)
