from flask import Flask
from dotenv import dotenv_values


class Settings:
    SPOTIFY_CLIENT_ID = ""
    SPOTIFY_CLIENT_SECRET = ""
    SPOTIFY_STATE = ""

    def init_app(self, app: Flask) -> None:
        config = dotenv_values()
        for key, value in config.items():
            self.__setattr__(key, value)

        app.config.from_object(self)


settings = Settings()
