from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, user_schema, users_schema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from datetime import timedelta
from models.team import Team, team_schema, teams_schema
from controllers.team_thread_controller import authorise_as_admin

# Create a Blueprint for handling authorisation
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Route to register a new user
@auth_bp.route('/register', methods=['POST'])
def auth_register(): # try except with psycopg2 errorcodes work here as you are entering new data
    try:
        # Get JSON data from the request body
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
        # Serialize the created user using user_schema and return as a JSON response with a 201 status code.
        return user_schema.dump(user), 201
    except IntegrityError as err:
        # Handle unique constraint violation (email and username should be unique)
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return { 'error': f'{err.orig.diag.message_detail}'}, 409
        # Handle not null constraint violation (required fields are missing)
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION: # serves as errorcode for not null violations
            return { 'error': f'The {err.orig.diag.column_name} is required' }, 409 # for whatever field that is null

# Route for user to login
@auth_bp.route('/login', methods=['POST'])
def auth_login():       # cannot use try, except and run psycopg2 as this data exists already as opposed to entering new data
    # Get JSON data from the request body
    body_data = request.get_json()
    # creates a variable that gets the email or username details from the JSON body_data inputted by user trying to login
    login_identifier = body_data.get('email') or body_data.get('username')
    # Find the user by email address or username
    user = User.query.filter(
        (User.email == login_identifier) | (User.username == login_identifier)
    ).first()

    # Check if user exists and if password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get('password')):
        # Generate a JWT token for the user
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        # Return user information along with the JWT token
        return { 'username': user.username,'email': user.email, 'token': token, 'is_admin': user.is_admin }
    # if username, email or password does not match the respective fields in the database
    else:
        # Return error saying the email, username or password is incorrect and to prompt user to try again with status code 401.
        return { 'error': 'Invalid email, username or password entered. Please try again!' }, 401

# Route for admin to delete users
@auth_bp.route('/users/<int:id>', methods=['DELETE'])
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def auth_delete_one_user(id):
    # Query the database to get the user with the specified id.
    stmt = db.select(User).filter_by(id=id)
    # Execute the query and return the result as a single user_to_delete object.
    user_to_delete = db.session.scalar(stmt)

    # If user_to_delete id has a matching id in the database
    if user_to_delete:
        # Delete the user and commit the changes to the database.
        db.session.delete(user_to_delete)
        db.session.commit()
        # Return a message to inform that the user with username was deleted successfully!
        return { 'message': f'User {user_to_delete.username} deleted successfully!'}
    # If user_to_delete id does not match any ids
    else:
        # Return an error saying the user with the id does not exist and cannot be deleted with status code 404 
        return { 'error': f'The user with id no.{id} does not exist and cannot be deleted!!!'}, 404

# Route for users to edit details about themselves
@auth_bp.route('/users/<int:id>', methods=['PUT', 'PATCH'])
# Require a valid JWT token to access this route
@jwt_required()
def update_one_user(id):
    # Load the JSON request data into a user_schema object for validation.
    # The partial=True argument indicates that the data is not required to include all fields, as it is a partial update.
    body_data = user_schema.load(request.get_json(), partial=True)
    # Query the database to get the user with the specified id.
    stmt = db.select(User).filter_by(id=id)
    # Execute the query and return the result as a single user_to_update object.
    user_to_update = db.session.scalar(stmt)
    
    # if the user_to_update exists and has a matching id in the database
    if user_to_update:
        # Get the user id from the JWT token and fetch the corresponding user from the database.
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        # Check if the user is the owner of the user profile being updated
        if user.id == user_to_update.id:
            user.name = body_data.get('name') or user.name
            user.email = body_data.get('email') or user.email
            user.username = body_data.get('username') or user.username
            user.favourite_player = body_data.get('favourite_player') or user.favourite_player
            user.team_id = body_data.get('team_id') or user.team_id
            # if there is a password entry in the JSON body_data inputted by user trying to update
            if body_data.get('password'):
                # encrypt the user password in the database
                user.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8') or user.password
            # commit any updated changes to be saved into the database
            db.session.commit()
            # Serialize the user_to_update using user_schema and return as a JSON response.
            return user_schema.dump(user_to_update)
        # If the user is not the owner of the user profile being updated
        else:
            # Return error indicating only user can edit his own details with status code 403
            return { 'error': 'Sorry! Only the user can edit his own details!'}, 403
    # if the user_to_update doest not exist as the id is not in the database
    else:
        # Return an error saying the user_to_update does not exist in the database and cannot be updated with status code 404
        return { 'error': f'The user with id no.{id} does not exist and cannot be updated!'}, 404