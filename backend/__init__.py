import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext

db = SQLAlchemy()

@click.command("db-init")
@with_appcontext
def db_init():
    db.create_all()
    
def init_app(app):
    app.cli.add_command(db_init)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    database_config = os.path.join(app.instance_path, 'demo_1.sqlite')
    app.config.from_mapping(DATABASE=database_config, SECRET_KEY="1234")
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py", silent=False)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    init_app(app)
    
    from backend.auth import auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
