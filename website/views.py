from flask import Blueprint, render_template
from .api import Api
import random
import pprint


views = Blueprint("views", __name__)


@views.route("/")
def index():
    unsplash_api = Api()
    images = format_api(unsplash_api.get_images())
    art_image = random.choice(unsplash_api.query("art", 1)["results"])
    return render_template("index.html", art_image=art_image["urls"]["full"], images=images)


def format_api(api: list):
    result = []
    for i in range(3):
        cols = []
        j = i
        while True:
            try:
                image = api[j]
                cols.append(image)
                j += 3
            except IndexError:
                break
        result.append(cols)
    return result
