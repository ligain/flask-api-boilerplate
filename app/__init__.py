from flask import Flask

from app.api import api
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api.init_app(app)
    return app
