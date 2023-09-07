import pytest
from api_tests.api.product_api import ProductAPI

API_BASE_URL = "https://automationexercise.com/api"


@pytest.fixture
def api_client():
    return ProductAPI(API_BASE_URL)


def test_status_code(api_client):
    response = api_client.get_all_products()
    print('Verify status code')
    assert response.status_code == 200


def test_content_type(api_client):
    response = api_client.get_all_products()
    print('Verify header Content-Type')
    assert "application/json" in response.headers["Content-Type"]


def test_response_code(api_client):
    response = api_client.get_all_products()
    data = response.json()
    print('Verify responseCode')
    assert data['responseCode'] == 200


def test_response_data(api_client):
    response = api_client.get_all_products()
    data = response.json()
    print('Verify the response is a valid json')
    assert isinstance(data, dict)
    print('Verify the products list is a valid list')
    assert isinstance(data['products'], list)
    print('Verify there are at least one product')
    assert len(data['products']) > 0  # There should be at least one product


def test_response_structure(api_client):
    response = api_client.get_all_products()
    data = response.json()
    print('Verify data structure')
    for product in data['products']:
        print(f"product id: {product['id']}")
        assert "id" in product
        assert "name" in product
        assert "price" in product
        assert "brand" in product
        assert "category" in product
        assert "usertype" in product['category']
        assert "usertype" in product['category']['usertype']
        assert "category" in product['category']


def test_response_time(api_client):
    sla = 1000
    response = api_client.get_all_products()
    print(f"Verify response time: {response.elapsed.total_seconds()}")
    response_time_ms = response.elapsed.total_seconds() * 1000  # Convert to milliseconds
    assert response_time_ms < sla  # Ensure response time is under the SLA
