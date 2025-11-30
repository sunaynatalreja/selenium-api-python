import pytest
from src.api.core.client import Client
from src.api.helpers import data_provider
from src.api.constants import constants
from http import HTTPStatus
import allure
from src.api.response.list_user_response import ListUserResponse


@pytest.fixture(scope="module")
def api():
    return Client()

@allure.title()
@allure.description("Verify that users are getting listed successfully")
def test_list_success(api):
    response = api.get(constants.USERS)
    list_response = ListUserResponse.model_validate(response.json())
    assert response.status_code == HTTPStatus.OK
    assert list_response.page == 1
    assert list_response.per_page>1
    assert list_response.total_pages>1
    assert len(list_response.data)>0
    assert list_response.total>1