from flask import Blueprint, render_template
from .api import Api
import random


views = Blueprint("views", __name__)


@views.route("/")
def index():
    unsplash_api = Api()
    images = unsplash_api.get_images()
    art_image = random.choice(unsplash_api.query("art", 1)["results"])
    return render_template("index.html", art_image=art_image["urls"]["full"], images=images)
