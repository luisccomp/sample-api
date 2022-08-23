from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


class IntegerPKMixin:
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)


def init_app(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
