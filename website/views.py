from flask import Blueprint, render_template, request, redirect, url_for
from .api import Api
import random


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("search")
        return redirect(url_for('views.result', query=query))
    unsplash_api = Api()
    page_on = random.randint(1, 5)
    images = format_api(unsplash_api.get_images())
    art_image = random.choice(unsplash_api.query("art", page_on)["results"])
    return render_template(
        "index.html",
        art_image=art_image["urls"]["full"],
        images=images
    )


@views.route("/result/<query>")
def result(query):
    unsplash_api = Api()
    page_on = random.randint(1, 5)
    images = format_api(unsplash_api.query(
        query=query, page_on=page_on)["results"])
    art_image = random.choice(unsplash_api.query("art", page_on)["results"])
    return render_template(
        "result.html",
        images=images,
        art_image=art_image["urls"]["full"]
    )


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
