import requests
import json
import os


class Api:
    def __init__(self):
        self.base_url = "https://api.unsplash.com"
        config_file = open(os.path.join(
            os.getcwd(), "website\\projectConfig.json"))
        self.unsplash_keys = json.load(config_file)
        self.access_key = self.unsplash_keys["access_key"]
        self.secret_key = self.unsplash_keys["secret_key"]

    def get_images(self):
        res = requests.get(
            self.base_url + f"/photos/?client_id={self.access_key}")
        return res.json()

    def query(self, query: str, page_on: int):
        res = requests.get(
            self.base_url + f"/search/photos?page={page_on}&query={query}&client_id={self.access_key}")
        return res.json()

    def get_image(self, id: str):
        res = requests.get(
            self.base_url + f"/search/photos/{id}?client_id={self.access_key}")
        return res.json()
