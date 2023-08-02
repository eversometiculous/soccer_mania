from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.comment_controller import comments_bp
from models.user import User
import functools

# Create a Blueprint for handling team threads
team_threads_bp = Blueprint('team_threads', __name__, url_prefix='/team_threads')

# Register the comments_bp (another Blueprint) as a sub-Blueprint for handling comments related to team threads
team_threads_bp.register_blueprint(comments_bp)

# Define a decorator function to authorize actions only for admin users
def authorise_as_admin(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # Get the user_id from the JWT token
        user_id = get_jwt_identity()
        # Query the database to get the user object
        stmt = db.select(User).filter_by(id=user_id)
        # Execute the query and return the result as a single user object.
        user = db.session.scalar(stmt)
        # Check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response.
        if user.is_admin:
            # Execute the function with its arguments and key word arguments
            return fn(*args, **kwargs)
        else:
            # Return an error response saying only the admin can perform this action with status code 403.
            return { 'error': 'Sorry! Only the admin can perform this action!'}, 403

    return wrapper

# Route to get all team threads
@team_threads_bp.route('/')
def get_all_team_threads():
    # Query the database to get all team threads and order them in descending order based on their id.
    stmt = db.select(Team_thread).order_by(Team_thread.id.desc())
    # Execute the query and return the results as a list of team thread objects.
    team_threads = db.session.scalars(stmt)
    # Serialize the list of team thread objects using team_threads_schema and return as a JSON response.
    return team_threads_schema.dump(team_threads)

# Route to get a specific team thread by its id
@team_threads_bp.route('/<int:id>')
def get_one_team_thread(id):
    # Query the database to get a team thread with the specified id.
    stmt = db.select(Team_thread).filter_by(id=id)
    # Execute the query and return the result as a single team thread object.
    team_thread = db.session.scalar(stmt)
    # Check if the team thread exists; if yes, serialize it using team_thread_schema and return as a JSON response.
    # If not found, return an error response with a 404 status code.
    if team_thread:
        return team_thread_schema.dump(team_thread)
    else:
        return { 'error': f'There is no existing team thread with id no.{id}!'}, 404

# Route to create a new team thread
@team_threads_bp.route('/', methods=['POST'])
# Require a valid JWT token to access this route
@jwt_required()
def create_team_thread():
    # Load the JSON request data into a team_thread_schema object for validation.
    body_data = team_thread_schema.load(request.get_json())  # team_thread_schema.load is required to do marshmallow validation(eg. 2 min characters).
    # Otherwise it will not bother with marshmallow min character length. If it just have body_data = request.get_json(), min characters wont matter.
    # Get the user_id from the JWT token
    user_id = get_jwt_identity()
    # Query the database to get the user object based on the user_id
    user = User.query.get(user_id)
    # Check if the user exists and has a team associated with them
    if not user:
        return { 'error': 'User not found'}, 404
    # check if user has a team associated with them
    if not user.team:
        return { 'error': 'User team not found'}, 404

    # Create a new Team_thread model instance with the data from the request
    team_thread = Team_thread(
        # sets the title attribute of the team_thread instance to the value obtained from the body_data dictionary.
        title=body_data.get('title'),
        # sets the description attribute of the team_thread instance to the value obtained from the body_data dictionary.
        description=body_data.get('description'),
        # set the team_thread to the date it was created(current date)
        date=date.today(),
        # It sets the user attribute of the team_thread instance to the user object obtained from the database. 
        # This associates the user who created the team thread with the newly created team thread
        user=user,
        # It sets the team attribute of the team_thread instance to the team object associated with the user. 
        # This links the team thread to the team that the user belongs to.
        team=user.team
    )
    # Add that team_thread to the session
    db.session.add(team_thread)
    # Commit the changes to the session.
    db.session.commit()
    # Serialize the created team_thread using team_thread_schema and return as a JSON response with a 201 status code.
    return team_thread_schema.dump(team_thread), 201

# Route to delete a specific team thread by its id
@team_threads_bp.route('/<int:id>', methods=['DELETE'])
# Require a valid JWT token to access this route
@jwt_required()
def delete_one_team_thread(id):
    # Get the user_id from the JWT token
    user_id = get_jwt_identity()
    # Query the database to get the user object based on the user_id
    user = User.query.get(user_id)
    # Query the database to get the team thread with the specified id
    stmt = db.select(Team_thread).filter_by(id=id)
    # Execute the query and return the result as a single team thread object.
    team_thread = db.session.scalar(stmt)

    if team_thread:
        # Check if the user is an admin or the creator of the team thread
        if str(team_thread.user_id) == user_id or user.is_admin:
            # deletes the thread if user is admin or creator of team thread
            db.session.delete(team_thread)
            # commits the deletion to the database
            db.session.commit()
            # returns message saying deletion successful
            return { 'message': f'Team thread {team_thread.title} deleted successfully!'}
        else:
            # Return an error response if the user is not authorized to delete the team thread
            return { 'error': 'Only the admin or the user who created the team thread can delete it!! Sorry!!'}, 403
    else:
        # Return an error response if the team thread does not exist at all
        return { 'error': f'Team thread with id no.{id} does not exist and cannot be deleted!!!'}, 404


# Route to update a specific team thread by its id
@team_threads_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
# Require a valid JWT token to access this route
@jwt_required()
def update_one_team_thread(id):
    # Load the JSON request data into a team_thread_schema object for validation. The partial=True argument 
    # indicates that the data is not required to include all fields, as it is a partial update.
    body_data = team_thread_schema.load(request.get_json(), partial=True)
    # Get the user_id from the JWT token
    user_id = get_jwt_identity()
    # Query the database to get the team thread with the specified id
    stmt = db.select(Team_thread).filter_by(id=id)
    # Execute the query and return the result as a single team thread object.
    team_thread = db.session.scalar(stmt)

    if team_thread:
        # Check if the user is the creator of the team thread
        if str(team_thread.user_id) != user_id:
            # Return an error response if the user is not authorized to edit the team thread
            return { 'error': 'Sorry! Only the person who created the team thread can edit the team thread!'}, 403
        # Update the team thread with the new data from the request and commit the changes
        # sets the title attribute of the team_thread instance to the value obtained from the body_data dictionary OR
        # sets the team_thread.title to the existing team_thread.title in the database if no input was made in title field
        team_thread.title = body_data.get('title') or team_thread.title
        # sets the description attribute of the team_thread instance to the value obtained from the body_data dictionary OR
        # sets the team_thread.description to the existing team_thread.description in the database if no 
        # input was made in description field
        team_thread.description = body_data.get('description') or team_thread.description
        # updates the team_thread to current date when it is editted
        team_thread.date_updated = date.today()
        # commit the changes to the database
        db.session.commit()
        # Serialize the updated team thread using team_thread_schema and return as a JSON response.
        return team_thread_schema.dump(team_thread)
    else:
        # Return an error response if the team thread with the specified id does not exist
        return { 'error': f'The team thread with id no.{id} does not exist and cannot be updated!'}, 404