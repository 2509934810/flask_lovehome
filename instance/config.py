import os


class BaseConfig(object):
    DEBUG = True
    DATA_PER_PAGE = 6


class DevConfig(BaseConfig):
    SECRET_KEY = "123456789"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.abspath(os.path.curdir)}/tmp/test.db"
    PERMANEXT_SESSION_LIFETIME = 3


class ProConfig(BaseConfig):
    SECRET_KEY = "123456789"
    DIALECT = "mysql"
    DRIVER = "pymysql"
    USERNAME = os.environ.get("USERNAME")
    PASSWORD = os.environ.get("PASSWORD")
    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    DATABASE = "lovehome"
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(
        DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    ARTICLES_PER_PAGE = 10
    COMMENTS_PER_PAGE = 6
    WTF_CSRF_SECRET_KEY = "random key for form"
