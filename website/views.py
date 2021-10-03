from flask import Blueprint, render_template
from .api import Api


views = Blueprint("views", __name__)


@views.route("/")
def index():
    unsplash_api = Api()
    print(unsplash_api.get_images())
    return render_template("index.html")
