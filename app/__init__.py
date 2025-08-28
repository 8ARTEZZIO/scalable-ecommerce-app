"""
Run the app
e.g. app = Flask(__name__)
initialize all the models
make sure it connects to the app
return create_app
"""
# app/__init__.py
from __future__ import annotations
import os
from datetime import datetime
from flask import Flask, render_template
from .extensions import db, migrate, login_manager, csrf
from .config import DevConfig, TestConfig, ProdConfig
from .models import Users

def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # 1) Config (choose by APP_ENV=dev|test|prod; defaults to dev)
    env = os.getenv("APP_ENV", "dev").lower()
    cfg = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}.get(env, DevConfig)
    app.config.from_object(cfg)

    # 2) Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)   # only used if you wire Flask-Login
    csrf.init_app(app)            # Flask-WTF/CSRF protection

    @login_manager.user_loader
    def load_user(user_id):
        return db.get_or_404(Users, user_id)
    
    # 3) Register blueprints
    from .api import bp as web_bp
    app.register_blueprint(web_bp)                 # HTML at "/"

    # Optional JSON API (only if you have app/api.py)
    try:
        from .api import bp as api_bp
        app.register_blueprint(api_bp, url_prefix="/api")
    except Exception:
        pass

    # 4) Import models so Alembic/Flask-Migrate can discover them
    from . import models  # noqa: F401

    # 5) Jinja globals & error pages
    @app.context_processor
    def inject_year():
        return {"year": datetime.utcnow().year}

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app
