from flask import Blueprint, request
from init import db
from models.team_thread import team_thread_schema, team_threads_schema
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp
from models.team import Team, team_schema, teams_schema
from models.user import User
from models.manager import Manager, manager_schema, managers_schema
from controllers.team_thread_controller import authorise_as_admin

# Create a Blueprint for handling managers
managers_bp = Blueprint('managers', __name__, url_prefix='/managers')

# Route to get all managers
@managers_bp.route('/')
def get_all_managers():
    # Query the database to get all managers and order them in descending order based on their id.
    stmt = db.select(Manager).order_by(Manager.id.desc())
    # Execute the query and return the results as a list of manager objects.
    managers = db.session.scalars(stmt)
    # Serialize the list of manager objects using managers_schema and return as a JSON response.
    return managers_schema.dump(managers)

# Route to get a specific manager by its id
@managers_bp.route('/<int:id>')
def get_one_manager(id):
    # Query the database to get a manager with the specified id.
    stmt = db.select(Manager).filter_by(id=id)
    # Execute the query and return the result as a single manager object.
    manager = db.session.scalar(stmt)
    # Check if the manager exists; if yes, serialize it using manager_schema and return as a JSON response.
    # If not found, return an error response with a 404 status code.
    # if manager exists
    if manager:
        # Serialize the manager objects using manager_schema and return as a JSON response
        return manager_schema.dump(manager)
    # if manager does not exist
    else:
        # Return a error message saying no existing manager with that id no.
        return { 'error': f'There is no existing manager with id no.{id}!'}, 404
    
# Route to create a new manager
@managers_bp.route('/', methods=['POST'])
# Require a valid JWT token to access this route
@jwt_required()
def create_manager():
    # Load the JSON request data into a manager_schema object for validation.
    body_data = manager_schema.load(request.get_json())

    # Create a new Manager model instance and set its attributes based on the provided data from the request.
    # The attributes of the newly created manager (name, date_of_birth, teams_managed_previously, trophies_won, and team_id) 
    # are set based on the data from the validated JSON request (body_data). It uses body_data.get() to retrieve the values 
    # from body_data and assign them to the respective manager attributes.
    manager = Manager() # Instance of the Manager class which is in turn a SQLAlchemy model
    manager.name = body_data.get('name')
    manager.date_of_birth = body_data.get('date_of_birth')
    manager.teams_managed_previously = body_data.get('teams_managed_previously')
    manager.trophies_won = body_data.get('trophies_won')
    manager.team_id = body_data.get('team_id')
    # Add the new manager to the session and commit the changes to the database.
    db.session.add(manager)
    db.session.commit()
    # Serialize the created manager using manager_schema and return as a JSON response with a 201 status code.
    return manager_schema.dump(manager), 201

# Route to delete a specific manager by its id
@managers_bp.route('/<int:id>', methods=['DELETE'])        # only admins can delete
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def delete_one_manager(id):
    # Query the database to get the manager with the specified id.
    stmt = db.select(Manager).filter_by(id=id)
    # Execute the query and return the result as a single manager object.
    manager = db.session.scalar(stmt)
    # if manager exists
    if manager:
        # Delete the manager from the database and commit the changes.
        db.session.delete(manager)
        db.session.commit()
        # Return a message response saying deletion was successful
        return { 'message': f'Manager {manager.name} deleted successfully!'}
    # if manager does not exist
    else:
        # Return an error response if the manager with the specified id does not exist.
        return { 'error': f'Manager with id no.{id} does not exist and cannot be deleted!!!'}, 404
    
# Route to update a specific manager by its id
@managers_bp.route('/<int:id>', methods=['PUT', 'PATCH'])           # only admins can edit or update
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def update_one_manager(id):
    # Load the JSON request data into a manager_schema object for validation.
    # The partial=True argument indicates that the data is not required to include all fields, as it is a partial update.
    body_data = manager_schema.load(request.get_json(), partial=True)
    # Query the database to get the manager with the specified id.
    stmt = db.select(Manager).filter_by(id=id)
    # Execute the query and return the result as a single manager object.
    manager = db.session.scalar(stmt)
    # if manager exists
    if manager:
        # Update the manager with the new data from the request and commit the changes.
        # Each line updates the corresponding attribute of the manager with the new value from the 
        # JSON request if available. If the attribute is missing or has an empty value in the JSON request, 
        # the line effectively updates the manager's attribute with its current value, ensuring that unchanged attributes 
        # are not modified during the update process. This is done by using OR.
        manager.name = body_data.get('name') or manager.name
        manager.date_of_birth = body_data.get('date_of_birth') or manager.date_of_birth
        manager.teams_managed_previously = body_data.get('teams_managed_previously') or manager.teams_managed_previously
        manager.trophies_won = body_data.get('trophies_won') or manager.trophies_won
        manager.team_id = body_data.get('team_id') or manager.team_id
        # commit the changes to the manager table in the database
        db.session.commit()
        # Serialize the updated manager using manager_schema and return as a JSON response.
        return manager_schema.dump(manager)
    # if manager does not exist
    else:
        # Return an error response if the manager with the specified id does not exist.
        return { 'error': f'The manager with id no.{id} does not exist and cannot be updated!'}, 404