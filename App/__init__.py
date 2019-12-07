from flask import Flask

from App import ext
from App.settings import envs
from App.views.index import web


def create_app():
    app = Flask(__name__)
    app.config.from_object(envs.get('develop'))
    ext.init_ext(app)
    app.register_blueprint(web)
    return app
