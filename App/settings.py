def get_db_uri(dbinfo):
    ENGINE = dbinfo.get("ENGINE") or 'mysql'
    DRIVER = dbinfo.get("DRIVER") or "pymysql"
    USER = dbinfo.get("USER") or "root"
    PASSWORD = dbinfo.get("PASSWORD") or "hyjkj1009"
    HOST = dbinfo.get("HOST") or "localhost"
    PORT = dbinfo.get("PORT") or "3306"
    NAME = dbinfo.get("NAME") or "fisher"

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config:

    DEBUG = False

    TESTING = False

    SECRET_KEY = "newboys"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):

    DEBUG = True

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "hyjkj1009",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "fisher"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

    MAIL_SERVER = "smtp.163.com"

    MAIL_PORT = 25

    MAIL_USERNAME = "xihonlin@163.com"
    # os.environ.get("MAIL_PASSWORD")
    MAIL_PASSWORD = "qhl930706"

    MAIL_DEFAULT_SENDER = "xihonlin@163.com"


class TestingConfig(Config):

    TESTING = True

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "hyjkj1009",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "fisher"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "hyjkj1009",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "fisher"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "hyjkj1009",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "fisher"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}