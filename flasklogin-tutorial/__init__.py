"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
sess = Session()


def create_app():
    """Construct the core flask_session_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    sess.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from .assets import compile_static_assets, compile_auth_assets
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        compile_static_assets(app)
        compile_auth_assets(app)

        db.create_all()

        if app.config['FLASK_ENV'] == 'development':
            compile_assets(app)

        return app