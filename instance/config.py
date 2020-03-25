import os
from datetime import timedelta


class BaseConfig(object):
    DEBUG = True
    DATA_PER_PAGE = 6
    AUTH_REDIS = "redis://localhost:6379/3"
    CELERY_BROKER_URL = ("redis://localhost:6379/1",)
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    CELERYBEAT_SCHEDULE = {
        # 定义任务名称：import_data
        # 执行规则：每600秒运行一次
        "import_data": {"task": "import_data", "schedule": timedelta(seconds=600)},
    }


class DevConfig(BaseConfig):
    SECRET_KEY = "123456789"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}/tmp/test.db".format(
        os.path.abspath(os.path.curdir)
    )
    PERMANEXT_SESSION_LIFETIME = 3


class ProConfig(BaseConfig):
    SECRET_KEY = "123456789"
    DIALECT = "mysql"
    DRIVER = "pymysql"
    USERNAME = os.environ.get("USERNAME")
    PASSWORD = os.environ.get("PASSWORD")
    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    DATABASE = os.environ.get("DATABASE")
    URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(
        DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
    )
    SQLALCHEMY_DATABASE_URI = URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    ARTICLES_PER_PAGE = 10
    COMMENTS_PER_PAGE = 6
    WTF_CSRF_SECRET_KEY = "random key for form"
