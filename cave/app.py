import os
from flask import Flask
from cave.views.health import health_blueprint
from cave.views.home import home_blueprint

CAVE_BLUEPRINTS = [
    health_blueprint,
    home_blueprint,
]


def create_app():
    app = Flask(__name__)

    config = os.environ.get("APP_CONFIG", "cave.config.DevelopmentConfig")
    app.config.from_object(config)

    for blueprint in CAVE_BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app
