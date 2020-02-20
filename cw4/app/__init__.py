from flask import Flask
from os.path import dirname, abspath, join
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KUiUAmxhPVN3YWXmG684Wg'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CWD = dirname(abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(CWD, 'rain.sqlite')
    db.init_app(app)
    with app.app_context():
        db.Model.metadata.reflect(db.engine)

    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
