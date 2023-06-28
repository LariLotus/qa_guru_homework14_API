import requests

from helper import CustomSession

ADD_TO_CARD_URL = "https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1"


class DemoQA:
    def __int__(self):
        self.base_url = "https://demowebshop.tricentis.com"
        self.authorization_cookie = None

    def login(self, email, password):
        response = requests.post(
            url=f"{self.base_url}/login",
            data={"Email": email, "Password": password},
            allow_redirects=False
        )
        self.authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        # return self

    def add_to_card(self, product="31/1/1", count=2):
        response = None
        for i in range(count):
            response = requests.post(
                url=f'{self.base_url}/addproducttocart/catalog/{product}',
                cookies={"NOPCOMMERCE.AUTH": self.authorization_cookie}
            )
        return response


class DemoQAWithSession:
    def __int__(self, url):
        self.demoqa_session = CustomSession(url)

    def login(self, email, password):
        self.demoqa_session.post(
            url="/login",
            data={"Email": email, "Password": password},
            allow_redirects=False
        )

    def add_to_card(self, product_id="31/1/1", count=2):
        response = None
        for i in range(count):
            response = self.demoqa_session.post(
                url=f'/addproducttocart/catalog/{product_id}'
            )
        return response
