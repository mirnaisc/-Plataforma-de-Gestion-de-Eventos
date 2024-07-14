from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import usuarios_routes, eventos_routes, registro_routes, notificaciones_routes
    app.register_blueprint(usuarios_routes.bp)
    app.register_blueprint(eventos_routes.bp)
    app.register_blueprint(registro_routes.bp)
    app.register_blueprint(notificaciones_routes.bp)

    return app
