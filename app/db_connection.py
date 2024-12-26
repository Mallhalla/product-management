# db_connection.py
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

def create_mongo_client():
    connection_string = os.environ.get("MONGO_CONNECTION_STRING")
    client = MongoClient(connection_string, server_api=ServerApi('1'))
    return client
