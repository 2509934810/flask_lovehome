import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext
from instance.config import DevConfig, ProConfig
from flask_redis import FlaskRedis
from flask_celery import Celery
from flask_cors import CORS

db = SQLAlchemy()
redis_store = FlaskRedis()
auth_store = FlaskRedis(config_prefix=ProConfig.AUTH_REDIS)
celery = Celery()


@click.command("db-init")
@with_appcontext
def db_init():
    db.create_all()


def init_app(app):
    app.cli.add_command(db_init)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.add_template_global(os.environ.get("FRONT_1"), "front1")
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object(ProConfig)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    init_app(app)

    redis_store.init_app(app)
    celery.init_app(app)
    # 注册auth redis
    auth_store.init_app(app)
    from backend.auth import auth_bp

    app.register_blueprint(auth_bp)

    from backend.User import user_bp

    app.register_blueprint(user_bp)

    from backend.admin import admin_bp

    app.register_blueprint(admin_bp)

    from backend.api import api_bp

    app.register_blueprint(api_bp)

    from backend.service import service_bp

    app.register_blueprint(service_bp)

    from backend.manage import manage_bp

    app.register_blueprint(manage_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/404")
    def pageNotFound():
        data = {"code": 404, "info": "page not found"}
        return jsonify(data)

    return app
