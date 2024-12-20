from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

def get_products():
    # Connect to DB
    connection_string = os.environ.get("MONGO_CONNECTION_STRING")
    client = MongoClient(connection_string, server_api=ServerApi('1'))

    try:
        db = client.product_inventory
        collection = db.products
        # Fetch all products from the collection
        products_cursor = collection.find()
        
        # Convert the cursor to a list and ensure ObjectId is serializable
        products_list = list(products_cursor)  # Convert cursor to list
        for product in products_list:
            # Manually convert ObjectId to string if needed
            product['_id'] = str(product['_id'])  # Convert ObjectId to string
        
        return products_list

    except Exception as e:
        print("Error:", e)
        return []

