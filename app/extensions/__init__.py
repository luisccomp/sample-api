from importlib import import_module

from flask import Flask


def load_extensions(app: Flask):
    for extension_path in app.config.get("EXTENSIONS", []):
        extension = import_module(extension_path)
        
        if hasattr(extension, "init_app"):
            extension.init_app(app)
