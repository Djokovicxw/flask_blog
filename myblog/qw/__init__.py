from flask import Flask, render_template, config
from flask_bootstrap import Bootstrap
from .db import init_extension
from .views import blog, auth
from .config import Dev


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.register_blueprint(blog.blog)
    app.register_blueprint(auth.auth)
    app.config.from_object(Dev)
    init_extension(app)
    return app
