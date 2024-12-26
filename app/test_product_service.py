import pytest
from unittest.mock import patch, MagicMock
from app.product_service import get_all_products

# Mock MongoDB
@pytest.fixture
def mock_mongo_client():
    # Create a mock MongoDB client
    mock_client = MagicMock()
    
    # Mock the database and collection
    mock_db = MagicMock()
    mock_collection = MagicMock()
    
    # Set up the mock to return a mock collection
    mock_client.product_inventory = mock_db
    mock_db.products = mock_collection
    
    # Set up the mock collection to return the mock data for the find() method
    mock_collection.find.return_value = [
        {'_id': '6742016d02a7a5bc19fe8461', 'name': 'hoodie-elephant', 'price': 2000, 'image': 'https://github.com/user-attachments/assets/45b191b0-4662-45ce-88b7-44ee10250b60'},
        {'_id': '6744554d4133dc4a912b884c', 'name': 'elephant', 'price': 4600000, 'image': 'https://github.com/user-attachments/assets/74edfc39-dae7-44be-b71c-3f7b67e739cb'}
    ]
    
    # Return the mock client to be used in the tests
    yield mock_client

def test_get_all_products(mock_mongo_client):
    # Call the function that fetches all products, passing in the mocked client
    products = get_all_products(client=mock_mongo_client)
    
    # Assertions to check if the returned products match the mock data
    assert len(products) == 2
    assert products[0]['_id'] == '6742016d02a7a5bc19fe8461'
    assert products[0]['name'] == 'hoodie-elephant'
    assert products[0]['price'] == 2000
    assert products[0]['image'] == 'https://github.com/user-attachments/assets/45b191b0-4662-45ce-88b7-44ee10250b60'
    assert products[1]['_id'] == '6744554d4133dc4a912b884c'
    assert products[1]['name'] == 'elephant'
    assert products[1]['price'] == 4600000
    assert products[1]['image'] == 'https://github.com/user-attachments/assets/74edfc39-dae7-44be-b71c-3f7b67e739cb'

def test_get_all_products_exception(mock_mongo_client):
    # Simulate an exception in the collection's find method
    mock_mongo_client.product_inventory.products.find.side_effect = Exception("Database error")

    # Call the function and expect an empty list due to the exception
    products = get_all_products(client=mock_mongo_client)

    # Assertions
    assert products == []