"""Initialize app."""
import profile

from flask import Flask
from flask_assets import Environment
import home.routes
from .assets import compile_assets
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_login import LoginManager
from pip._vendor.requests import Session

db = SQLAlchemy()
r = FlaskRedis
login_manager = LoginManager()
sess = Session()
assets = Environment()


def create_app():
    """Construct the core flask_session_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    login_manager.init_app(app)
    assets.init_app(app)

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)
    r.init_app(app)

    with app.app_context():
        from . import routes
        from .home, .profile, .products import routes
        from .profile import profile
        from .home import home
        from .products import products
        from app.main import routes
        from . import auth
        from .assets import compile_static_assets, compile_auth_assets

        app.register_blueprint(home.routes.home_bp)
        app.register_blueprint(profile.account_bp)
        app.register_blueprint(products.product_bp)
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(admin.admin_bp)
        compile_static_assets(app)
        compile_auth_assets(app)

        compile_static_assets(assets)

        db.create_all()

        if app.config['FLASK_ENV'] == 'development':
            compile_assets(app)


        return app