import os
from flask import Flask

def create_app(test_config=None):
    # Setup Application
    app = Flask(__name__, instance_relative_config=True, template_folder="view")

    # Configure Application
    app.config.from_mapping(SECRET_KEY='development_key_unsafe', DATABASE=os.path.join(app.instance_path, "database.sqlite"))
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register Database
    from .database.db import Database
    Database.register(app)

    # Register Blueprints
    from .controller import StoryController, ChapterController
    app.register_blueprint(StoryController.bp)
    app.register_blueprint(ChapterController.bp)

    # Register Routing
    app.add_url_rule("/", endpoint="story.read")

    return app