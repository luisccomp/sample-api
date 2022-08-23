from flask import Flask

from .exceptions import register_error_handlers
from .extensions import load_extensions
from .routes import register_routes
from .settings import Settings


app = Flask(__name__)
app.config.from_object(Settings)

load_extensions(app)
register_error_handlers(app)
register_routes(app)
