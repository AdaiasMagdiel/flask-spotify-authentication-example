from flask import Flask
from app.routes import site, auth


class Router:
    def __init__(self, app: Flask) -> None:
        app.register_blueprint(auth.bp)
        app.register_blueprint(site.bp)
