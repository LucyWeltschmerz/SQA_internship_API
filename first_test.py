import pytest
import requests
import json
import jsonpath


def test_get_authors():

    base_url = "https://fakerestapi.azurewebsites.net"
    endpoint = "/api/v1/Authors"

    response = requests.get(base_url + endpoint)
    assert response.status_code == 200


def test_post_authors():

    request_json = {
        "id": 603,
        "idBook": 2,
        "firstName": "First Name 603",
        "lastName": "Last Name 603"
    }
    base_url = "https://fakerestapi.azurewebsites.net"
    endpoint = "/api/v1/Authors"

    response = requests.post(base_url + endpoint, json=request_json)
    assert response.status_code == 200


@pytest.mark.parametrize("id_book", ["1", "20", "40"])
def test_get_authors_by_idbook(id_book):

    base_url = "https://fakerestapi.azurewebsites.net"
    endpoint = "/api/v1/Authors/authors/books/"

    response = requests.get(base_url + endpoint + id_book)
    assert response.status_code == 200


@pytest.mark.parametrize("author_id", ["1", "15", "30"])
def test_get_authors_by_id(author_id):

    base_url = "https://fakerestapi.azurewebsites.net"
    endpoint = "/api/v1/Authors/"

    response = requests.get(base_url + endpoint + author_id)
    assert response.status_code == 200


@pytest.mark.parametrize("author_id", ["15"])
def test_put_authors_by_id(author_id):
    
    base_url = "https://fakerestapi.azurewebsites.net"
    endpoint = "/api/v1/Authors/"

    request_json = {
        "id": 15,
        "idBook": 16,
        "firstName": "Example Name 15",
        "lastName": "Example Last Name 15"
    }

    response = requests.put(base_url + endpoint + author_id, json=request_json)
    assert response.status_code == 200


@pytest.mark.parametrize("author_id", ["1", "15", "30"])
def test_delete_author_by_id(author_id):

    base_url = "https://fakerestapi.azurewebsites.net"
    endpoint = "/api/v1/Authors/"

    response = requests.delete(base_url + endpoint + author_id)
    assert response.status_code == 200
