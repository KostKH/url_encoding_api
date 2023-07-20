import pytest
from fastapi.testclient import TestClient

from main import app
from tests.conftest import testing_urls, urls_with_error

client = TestClient(app)


@pytest.mark.parametrize('url_input, url_expected', testing_urls)
def test_encode(url_input, url_expected):
    input_json = {'url': url_input}
    expected_json = {'url': url_expected}
    response = client.post(url='/encode', json=input_json)
    assert response.status_code == 200
    assert response.json() == expected_json


@pytest.mark.parametrize('incorrect_url', urls_with_error)
def test_error_in_url(incorrect_url):
    input_json = {'url': incorrect_url}
    response = client.post(url='/encode', json=input_json)
    assert response.status_code == 422
    assert response.json()['detail'][0]['type'] == 'value_error'
    assert response.json()['detail'][0]['loc'] == ['body', 'url']


def test_error_empty_body():
    input_json = {}
    response = client.post(url='/encode', json=input_json)
    assert response.status_code == 422
    assert response.json()['detail'][0]['type'] == 'missing'
    assert response.json()['detail'][0]['loc'] == ['body', 'url']


def test_error_no_body():
    response = client.post(url='/encode')
    assert response.status_code == 422
    assert response.json()['detail'][0]['type'] == 'missing'
    assert response.json()['detail'][0]['loc'] == ['body']


def test_wrong_method():
    response = client.get(url='/encode')
    assert response.status_code == 405
    assert response.json()['detail'] == 'Method Not Allowed'
