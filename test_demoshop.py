import requests
from allure_commons._allure import step

from model.demoqa import DemoQA, DemoQAWithSession

ADD_TO_CARD_URL = "https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1"
LOGIN = "evalari91@gmail.com"
PASSWORD = "evalari91"


def test_add_to_card_response():
    with step("Авторизуемся"):
        response = requests.post(
            "https://demowebshop.tricentis.com/login",
            data={"Email": LOGIN, "Password": PASSWORD},
            allow_redirects=False
        )

    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    # авторизоваться
    # добавить товар в корзину

    with step("Добавляем товар в корзину"):
        result = requests.post(ADD_TO_CARD_URL, cookies={"NOPCOMMERCE.AUTH": authorization_cookie})

    with step("Проверяем, что продукт добавлен"):
        assert result.json()['success'] is True
        assert "The product has been added" in result.json()['message']
        assert result.json()["updatetopcartsectionhtml"] == "(4)"


def test_add_to_cart_response_with_model():
    with step("Авторизуемся"):
        demoqa = DemoQA()
        demoqa.login(email=LOGIN, password=PASSWORD)

    with step("Добавляем товаар в корзину"):
        result = demoqa.add_to_cart()

    with step("Провряем что продукт добавлен"):
        assert result.json()['success'] is True
        assert "The product has been added" in result.json()['message']
        assert result.json()["updatetopcartsectionhtml"] == "(4)"


def test_add_to_card_response_with_model_and_session(demoqa_url):
    with step("Авторизуемся"):
        demoqa = DemoQAWithSession(demoqa_url)
        demoqa.login(email=LOGIN, password=PASSWORD)

    with step("Добавляем товар в корзину"):
        result = demoqa.add_to_card()

    with step("Проверяем, что продукт добавлен"):
        assert result.json()['success'] is True
        assert "The product has been added" in result.json()['message']
        assert result.json()["updatetopcartsectionhtml"] == "(4)"
