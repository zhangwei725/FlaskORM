from flask import Flask

from app.ext import init_ext
from app.shop.views import shop
from app.user.views import user

app = Flask(__name__)
app.debug = True


def create_app():
    init_ext(app=app)
    register_blue()
    return app


def register_blue():
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(shop, url_prefix='/shop')
