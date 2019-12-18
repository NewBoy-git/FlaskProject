from .import api

@api.route('/index')
def hello_world():
    return 'Hello World!'
