import os

from dotenv import load_dotenv
from flask import Flask

from app.extensions import imp, db

load_dotenv()

DEV_MODE = True if os.environ.get("DEV_MODE") else False
# os.environ["SECRET_KEY"] = os.urandom(110).hex()
os.environ["SECRET_KEY"] = "flaskcon2023"


def create_app():
    app = Flask(__name__)
    imp.init_app(app)
    db.init_app(app)
    imp.import_models("models")

    imp.import_app_resources(
        app_factories=["dev_cli"] if DEV_MODE else [],
    )

    imp.import_blueprints("blueprints/backend")
    imp.import_blueprints("blueprints/frontend")

    with app.app_context():
        db.create_all()

    if DEV_MODE:
        print("DEV_MODE is enabled. Remember to turn this off in production (unset DEV_MODE)")

    return app
