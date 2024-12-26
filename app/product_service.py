from dotenv import load_dotenv
from app.db_connection import create_mongo_client

load_dotenv()

def get_all_products(client=None):
    if client is None:
        client = create_mongo_client()

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