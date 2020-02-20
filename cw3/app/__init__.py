from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

db = SQLAlchemy()


def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)



    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
