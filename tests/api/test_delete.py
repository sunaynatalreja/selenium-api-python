import pytest
from src.api.core.client import Client
from src.api.helpers import data_provider
from src.api.constants import constants
from http import HTTPStatus
import allure

from src.api.response.create_response import CreateResponse


@pytest.fixture(scope="module")
def api():
    return Client()

@allure.description("Verify that user is deleted successfully")
def test_delete_success(api):
    data=data_provider.get_delete_data()
    url=constants.USERS+"/"+str(data[0]['Id'])
    response = api.delete(url)
    assert response.status_code == HTTPStatus.NO_CONTENT

@allure.description("Verify that unauthorized user is unable to delete")
def test_delete_failure(api):
    data=data_provider.get_delete_data()
def test_delete_unauthorized(api):
    data=data_provider.get_delete_data()
    url=constants.USERS+"/"+str(data[1]['Id'])
    response = api.delete(url)
    assert response.status_code == HTTPStatus.UNAUTHORIZED