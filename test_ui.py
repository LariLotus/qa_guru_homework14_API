import logging
import time

import requests
from selene.support.conditions import have
from selene.support.shared import browser

from allure import step

LOGIN = "evalari91@gmail.com"
PASSWORD = "evalari91"


def test_login():
    """Successful authorization to some demowebshop (UI)"""
    with step("Open login page"):
        browser.open("http://demowebshop.tricentis.com/login")

    with step("Fill login form"):
        browser.element("#Email").send_keys(LOGIN)
        browser.element("#Password").send_keys(PASSWORD).press_enter()

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))


def test_login_through_api():
    with step("Open login page"):
        response = requests.post("http://demowebshop.tricentis.com/login",
                                 data={"Email": LOGIN, "Password": PASSWORD},
                                 allow_redirects=False)
        logging.info(response.status_code)
        logging.info(response.cookies.get("NOPCOMMERCE.AUTH"))
        authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        logging.info(authorization_cookie)
        browser.open("http://demowebshop.tricentis.com/login")

    with step("Verify successful authorization"):
        browser.open('http://demowebshop.tricentis.com/login')
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
        browser.open('http://demowebshop.tricentis.com/login')
        time.sleep(10)
        browser.element(".account").should(have.text(LOGIN))


def test_login_through_api_with_cookie_fixture(authorized_cookie):
    with step("Open shop with authorized user"):
        browser.open('http://demowebshop.tricentis.com/')
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorized_cookie})
        browser.open('http://demowebshop.tricentis.com/')

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))

