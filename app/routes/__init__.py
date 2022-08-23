from flask import Flask

from ..users.views import users_blueprint
from . import resources


def register_routes(app: Flask):
    app.register_blueprint(
        users_blueprint, url_prefix=resources.USERS_RESOURCE)
