"""
Run the app
e.g. app = Flask(__name__)
initialize all the models
make sure it connects to the
app's main functions
return app
"""
# app/__init__.py
import os
from datetime import datetime
from flask import Flask, render_template
from .extensions import db, migrate, login_manager, csrf
from .config import DevConfig, ProdConfig
from .models import User
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv; load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # 1) Config (choose by APP_ENV=dev|test|prod; defaults to dev)
    env = os.getenv("APP_ENV", "dev").lower()
    cfg = {"dev": DevConfig, "prod": ProdConfig}.get(env, DevConfig)
    app.config.from_object(cfg)

    # 2) Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)   # only used if you wire Flask-Login
    csrf.init_app(app)            # Flask-WTF/CSRF protection
    bootstrap = Bootstrap5(app)

    # 3) Load a Login Manager
    @login_manager.user_loader
    def load_user(user_id):
        try:
            return db.session.get(User, int(user_id))
        except (TypeError, ValueError):
            return None

    # 4) Register blueprints
    from .api import bp as api_bp
    app.register_blueprint(api_bp)                 # HTML at "/"
    from .web import bp as web_bp
    app.register_blueprint(web_bp)

    # 5) Import models so Flask-Migrate can discover them
    from . import models

    # 6) error pages
    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app
