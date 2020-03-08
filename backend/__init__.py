import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext
from instance.config import DevConfig
from flask_redis import FlaskRedis
from flask_celery import Celery

db = SQLAlchemy()
redis_store = FlaskRedis()
celery = Celery()


@click.command("db-init")
@with_appcontext
def db_init():
    db.create_all()


def init_app(app):
    app.cli.add_command(db_init)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object(DevConfig)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    init_app(app)

    redis_store.init_app(app)
    celery.init_app(app)

    from backend.auth import auth_bp

    app.register_blueprint(auth_bp)

    from backend.User import user_bp

    app.register_blueprint(user_bp)

    from backend.admin import admin_bp

    app.register_blueprint(admin_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
