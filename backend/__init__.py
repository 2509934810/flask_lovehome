import os
from flask import Flask


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

    # from backend.database import db_session
    # @app.teardown_appcontext
    # def close_db(exception=None):
    #     db_session.remove()

    from backend.auth import auth_bp
    app.register_blueprint(auth_bp)
    return app
