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

@allure.description("Verify that user is created successfully")
def test_create_success(api):
    data=data_provider.get_create_data()
    response = api.post(constants.USERS,data)
    assert response.status_code == HTTPStatus.CREATED
    create_response=CreateResponse.model_validate(response.json()[0])
    assert create_response.Job == data[0]['Job']
    assert create_response.Name == data[0]['Name']

@allure.description("Verify that unauthorized user is unable to create")
def test_create_unauthorized(api):
    data=data_provider.get_create_data()
    response = api.post(constants.USERS,data,headers={})
    assert response.status_code == HTTPStatus.UNAUTHORIZED