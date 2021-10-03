from flask import Flask


def start_app():
    from .views import views
    app = Flask(__name__)
    app.register_blueprint(views)
    return app
