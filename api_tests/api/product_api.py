import requests


class ProductAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_products(self):
        url = f"{self.base_url}/productsList"
        print(f'Calling api {url}')
        response = requests.get(url)
        return response
