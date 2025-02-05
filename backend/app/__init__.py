import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, send_from_directory, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from sqlalchemy import text
from flask_migrate import Migrate
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()
db = SQLAlchemy()

class Config:
    """App configuration variables."""
    if os.getenv("FLASK_ENV") == "development":
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "local.db")

    else:
        POSTGRES_URI = os.getenv("POSTGRES_URI")
        SQLALCHEMY_DATABASE_URI = POSTGRES_URI
    print(SQLALCHEMY_DATABASE_URI)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=4)


def create_app():
    """
    Creates and configures the Flask application.
    """
    # Initialize Flask without static folder
    app = Flask(__name__, static_folder=None)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)

    # Set up the frontend build directory path
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend/build"))
    
    db.init_app(app)
    with app.app_context():
        if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
            db.session.execute(text('PRAGMA foreign_keys=ON'))

    JWTManager(app)
    Migrate(app, db)
    setup_logging(app)

    # Register API routes
    from .routes.auth_routes import auth_bp
    from .routes.user_routes import user_bp
    from .routes.product_routes import product_bp
    from .routes.health_routes import health_bp

    # Register blueprints without additional prefix since they already have their own
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(health_bp)

    # Serve static files
    @app.route('/static/<path:path>')
    def serve_static(path):
        return send_from_directory(os.path.join(frontend_dir, 'static'), path)

    # Serve other static assets from root directory
    @app.route('/<path:path>')
    def serve_files(path):
        if os.path.exists(os.path.join(frontend_dir, path)):
            return send_from_directory(frontend_dir, path)
        return serve_react_app('')

    # Serve index.html and inject configuration
    @app.route('/', defaults={'path': ''})
    def serve_react_app(path):
        try:
            with open(os.path.join(frontend_dir, 'index.html'), 'r') as f:
                content = f.read()
            
            # Get backend URL from environment
            backend_url = os.getenv('REACT_APP_BACKEND_SERVER', f'http://localhost:{os.getenv("PORT", "8081")}')
            
            # Inject the configuration
            content = content.replace(
                'window.__RUNTIME_CONFIG__={BACKEND_URL:"{{BACKEND_URL}}"}',
                f'window.__RUNTIME_CONFIG__={{BACKEND_URL:"{backend_url}"}}'
            )
            
            return content, 200, {'Content-Type': 'text/html'}
        except Exception as e:
            app.logger.error(f"Error serving index.html: {str(e)}")
            return str(e), 500

    return app


def setup_logging(app):
    """
    Set up logging to a file, creating the log file if it doesn't exist.
    Logs will rotate when they reach a certain size.
    """
    if not os.path.exists('logs'):
        os.mkdir('logs')

    log_file = 'logs/app.log'

    file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
