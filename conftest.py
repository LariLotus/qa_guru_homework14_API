import logging

import pytest
import requests

LOGIN = "evalari91@gmail.com"
PASSWORD = "evalari91"
URL = "http://demowebshop.tricentis.com/login"


def pytest_addoption(parser):
    parser.addoption("--demoqa_url")


@pytest.fixture(scope='session')
def demoqa_url(request):
    return request.config.getoption("--demoqa_url")



@pytest.fixture()
def authorized_cookie():
    response = requests.post(
        url=URL,
        data={"Email": LOGIN, "Password": PASSWORD},
        allow_redirects=False
    )
    logging.info(response.status_code)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return authorization_cookie


@pytest.fixture
def auth_cookie():
    response = requests.post(
        "http://demowebshop.tricentis.com/login",
        data={"Email": LOGIN, "Password": PASSWORD},
        allow_redirects=False
    )
    logging.info(response.status_code)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return authorization_cookie
