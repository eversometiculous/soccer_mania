from flask import Flask
import os
from init import db, ma, bcrypt, jwt
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
from controllers.team_thread_controller import team_threads_bp
from marshmallow.exceptions import ValidationError
from controllers.user_controller import users_bp
from controllers.team_controller import teams_bp
from controllers.manager_controller import managers_bp
from controllers.player_controller import players_bp
from controllers.stadium_controller import stadiums_bp

def create_app():
    app = Flask(__name__)
    
    # Set the JSON sorting behavior to False to preserve the order of keys in JSON responses where ordered=True for fields
    app.json.sort_keys = False

    # Configure the app with the database URI and JWT secret key from environment variables. The os 
    # environment will grab the details for "DATABASE_URL" and "JWT_SECRET_KEY" from .env which stands for .environment
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    # Error handler for Marshmallow validation errors will return the error messages it finds with a 400 status code.
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return { 'error': err.messages}, 400

    # this app will handle 400 error and return the error as Bad request with 400 status code
    @app.errorhandler(400)
    def bad_request(err):
        return { 'error': str(err)}, 400
    
    # this app will handle 404 error and return the error as Not found with 404 status code
    @app.errorhandler(404)
    def not_found(err):
        return { 'error': str(err)}, 404
    
    # this app will handle 403 error and return the error as Forbidden with 403 status code
    @app.errorhandler(403)
    def not_found(err):
        return { 'error': str(err)}, 403
    
    # this app will handle 408 error and return the error as Request Timeout with 408 status code
    @app.errorhandler(408)
    def not_found(err):
        return { 'error': str(err)}, 408
    

    # To initialize Flask app with database, Marshmallow, bcrypt, and JWT extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register Blueprint for CLI database commands.
    app.register_blueprint(db_commands)

    # Register Blueprint for authentication-related endpoints.
    app.register_blueprint(auth_bp)

    # Register Blueprint for team thread-related endpoints.
    app.register_blueprint(team_threads_bp)

    # Register Blueprint for user-related endpoints.
    app.register_blueprint(users_bp)

    # Register Blueprint for team-related endpoints.
    app.register_blueprint(teams_bp)

    # Register Blueprint for manager-related endpoints.
    app.register_blueprint(managers_bp)

    # Register Blueprint for stadium-related endpoints.
    app.register_blueprint(stadiums_bp)

    # Register Blueprint for player-related endpoints.
    app.register_blueprint(players_bp)

    return app