from sanic import Sanic
from saphyr.dev import logo


def init(config):
    app = Sanic()
    app.static('/static', './static')
    app.config.LOGO = logo
    return app
