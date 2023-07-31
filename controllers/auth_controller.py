from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, user_schema, users_schema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from datetime import timedelta
from models.team import Team, team_schema, teams_schema
from controllers.team_thread_controller import authorise_as_admin

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def auth_register(): # try except with psycopg2 errorcodes work here as you are entering new data
    try:
        body_data = request.get_json()

        # Create a new User model instance from the user info
        user = User() # Instance of the User class which is in turn a SQLAlchemy model
        user.name = body_data.get('name')
        user.email = body_data.get('email')
        user.username = body_data.get('username')
        user.favourite_player = body_data.get('favourite_player')
        user.team_id = body_data.get('team_id')
        if body_data.get('password'):
            user.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')
        # Add the user to the session
        db.session.add(user)
        # Commit to add the user to the database
        db.session.commit()
        # Respond to the client
        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return { 'error': f'{err.orig.diag.message_detail}'}, 409
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION: # serves as errorcode for not null violations
            return { 'error': f'The {err.orig.diag.column_name} is required' }, 409 # for whatever field that is null
        
@auth_bp.route('/login', methods=['POST'])
def auth_login():       # cannot use try, except and run psycopg2 as this data exists already as opposed to entering new data
    body_data = request.get_json()
    login_identifier = body_data.get('email') or body_data.get('username')
    # Find the user by email address or username
    user = User.query.filter(
        (User.email == login_identifier) | (User.username == login_identifier)
    ).first()

    # Check if user exists and if password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get('password')):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return { 'username': user.username,'email': user.email, 'token': token, 'is_admin': user.is_admin }
    else:
        return { 'error': 'Invalid email or password entered. Please try again!' }, 401
     
@auth_bp.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
@authorise_as_admin
def auth_delete_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user_to_delete = db.session.scalar(stmt)

    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        return { 'message': f'User {user_to_delete.username} deleted successfully!'}
    else:
        return { 'error': f'The user with id no.{id} does not exist and cannot be deleted!!!'}, 404
    
@auth_bp.route('/users/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_user(id):
    body_data = user_schema.load(request.get_json(), partial=True)
    stmt = db.select(User).filter_by(id=id)
    user_to_update = db.session.scalar(stmt)

    if user_to_update:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        # Check if the user is the owner of the user profile being updated
        if user.id == user_to_update.id:
            user.name = body_data.get('name') or user.name
            user.email = body_data.get('email') or user.email
            user.username = body_data.get('username') or user.username
            user.favourite_player = body_data.get('favourite_player') or user.favourite_player
            user.team_id = body_data.get('team_id') or user.team_id
            if body_data.get('password'):
                user.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8') or user.password
            db.session.commit()
            return user_schema.dump(user_to_update)
        else:
            return { 'error': 'Sorry! Only the user can edit his own details!'}, 403
    else:
        return { 'error': f'The user with id no.{id} does not exist and cannot be updated!'}, 404
