from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required
from models.stadium import Stadium, stadium_schema, stadiums_schema
from controllers.team_thread_controller import authorise_as_admin

# Create a Blueprint for handling stadiums
stadiums_bp = Blueprint('stadiums', __name__, url_prefix='/stadiums')

# Route to get all stadiums
@stadiums_bp.route('/')
def get_all_stadiums():
    # Query the database to get all stadiums and order them in descending order based on their id.
    stmt = db.select(Stadium).order_by(Stadium.id.desc())
    # Execute the query and return the results as a list of stadium objects.
    stadiums = db.session.scalars(stmt)
    # Serialize the list of stadium objects using stadiums_schema and return as a JSON response.
    return stadiums_schema.dump(stadiums)

# Route to get a specific stadium by its id
@stadiums_bp.route('/<int:id>')
def get_one_stadium(id):
    # Query the database to get a stadium with the specified id.
    stmt = db.select(Stadium).filter_by(id=id)
    # Execute the query and return the result as a single stadium object.
    stadium = db.session.scalar(stmt)
    # Check if the stadium exists; if yes, serialize it using stadium_schema and return as a JSON response.
    # If not found, return an error response with a 404 status code.
    if stadium:
        return stadium_schema.dump(stadium)
    # if stadium does not exist
    else:
        return { 'error': f'There is no existing stadium with id no.{id}!'}, 404

# Route to create a new stadium
@stadiums_bp.route('/', methods=['POST']) 
# Require a valid JWT token to access this route   
@jwt_required()
def create_stadium():
    # Load the JSON request data into a stadium_schema object for validation.
    body_data = stadium_schema.load(request.get_json())

    # Create a new Stadium model instance and set its attributes based on the provided data from the request.
    stadium = Stadium() # Instance of the Stadium class which is in turn a SQLAlchemy model
    # A new Stadium model instance is created, and its attributes (stadium_name, location, year_built, and team_id) 
    # are set based on the data from the validated JSON request (body_data). 
    # The body_data.get() method is used to retrieve the values from the body_data dictionary.
    stadium.stadium_name = body_data.get('stadium_name')
    stadium.location = body_data.get('location')
    stadium.year_built = body_data.get('year_built')
    stadium.team_id = body_data.get('team_id')
    # Add the new stadium to the session and commit the changes to the database.
    db.session.add(stadium)
    # Commit to add the stadium to the database
    db.session.commit()
    # Serialize the created stadium using stadium_schema and return as a JSON response with a 201 status code.
    return stadium_schema.dump(stadium), 201

# Route to delete a specific stadium by its id
@stadiums_bp.route('/<int:id>', methods=['DELETE'])        # only admins can delete
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def delete_one_stadium(id):
    # Query the database to get the stadium with the specified id.
    stmt = db.select(Stadium).filter_by(id=id)
    # Execute the query and return the result as a single stadium object.
    stadium = db.session.scalar(stmt)
    # check if stadium exists
    if stadium:
        # Delete the stadium from the database and commit the changes.
        db.session.delete(stadium)
        db.session.commit()
        # return the message of a successful deletion.
        return { 'message': f'Stadium {stadium.stadium_name} deleted successfully!'}
    # else if stadium does not exist
    else:
        # Return an error response if the stadium with the specified id does not exist.
        return { 'error': f'Stadium with id no.{id} does not exist and cannot be deleted!!!'}, 404
    

# Route to update a specific stadium by its id
@stadiums_bp.route('/<int:id>', methods=['PUT', 'PATCH'])           # only admins can edit or update
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def update_one_stadium(id):
    # Load the JSON request data into a stadium_schema object for validation.
    # The partial=True argument indicates that the data is not required to include all fields, as it is a partial update.
    body_data = stadium_schema.load(request.get_json(), partial=True)
    # Query the database to get the stadium with the specified id.
    stmt = db.select(Stadium).filter_by(id=id)
    # Execute the query and return the result as a single stadium object.
    stadium = db.session.scalar(stmt)
    # if stadium exists
    if stadium:
        # Update the stadium with the new data from the request and commit the changes.
        # If the stadium with the specified ID exists, the code updates the stadium attributes 
        # (stadium_name, location, year_built, and team_id) with the new data from the validated JSON request (body_data). 
        # It uses body_data.get() to retrieve the values from body_data and update only the fields present in the JSON data.
        # The OR will indicate that there has been no input in that specific field and will leave the field in the database unchanged.
        stadium.stadium_name = body_data.get('stadium_name') or stadium.stadium_name
        stadium.location = body_data.get('location') or stadium.location
        stadium.year_built = body_data.get('year_built') or stadium.year_built
        stadium.team_id = body_data.get('team_id') or stadium.team_id

        db.session.commit()
        # Serialize the updated stadium using stadium_schema and return as a JSON response.
        return stadium_schema.dump(stadium)
    # if stadium does not exist
    else:
        # Return an error response if the stadium with the specified id does not exist.
        return { 'error': f'The stadium with id no.{id} does not exist and cannot be updated!'}, 404