from os import getenv

from dotenv import load_dotenv


if (environment := getenv("ENVIRONMENT", "development")) != "production":
    load_dotenv(
        ".env" if environment != "test" else ".env.test", override=True)


class Settings:
    EXTENSIONS = [
        "app.extensions.database",
        "app.extensions.bcrypt",
    ]
    
    API_VERSION = getenv("API_VERSION", "v1")
    
    SQLALCHEMY_DATABASE_URI = getenv(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
