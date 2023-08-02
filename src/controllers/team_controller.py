from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required
from models.team import Team, team_schema, teams_schema
from controllers.team_thread_controller import authorise_as_admin

# Create a Blueprint for handling teams
teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

# Route to get all teams
@teams_bp.route('/')
def get_all_teams():
    # Query the database to get all teams and order them in descending order based on their id.
    stmt = db.select(Team).order_by(Team.id.desc())
    # Execute the query and return the results as a list of team objects.
    teams = db.session.scalars(stmt)
    # Serialize the list of team objects using teams_schema and return as a JSON response.
    return teams_schema.dump(teams)

# Route to get a specific team by its id
@teams_bp.route('/<int:id>')
def get_one_team(id):
    # Query the database to get a team with the specified id.
    stmt = db.select(Team).filter_by(id=id)
    # Execute the query and return the result as a single team object.
    team = db.session.scalar(stmt)
    # Check if the team exists; if yes, serialize it using team_schema and return as a JSON response.
    # If not found, return an error response with a 404 status code.
    if team:
        return team_schema.dump(team)
    else:
        return { 'error': f'There is no existing team with id no.{id}!'}, 404

# Route to create a new team
@teams_bp.route('/', methods=['POST'])
# Require a valid JWT token to access this route
@jwt_required()
def create_team():
    # Load the JSON request data into a team_schema object for validation.
    body_data = team_schema.load(request.get_json())

    # Create a new Team model instance and set its attributes based on the data from the request
    team = Team() # Instance of the Team class which is in turn a SQLAlchemy model
    # These lines set the attributes of the team instance using the data from the body_data dictionary. 
    # The body_data.get('team_name') retrieves the value of the 'team_name' field from the validated data and assigns 
    # it to the team_name attribute of the team instance
    team.team_name = body_data.get('team_name')
    # Similarly, the 'trophies_won' value from the body_data dictionary is assigned to the trophies_won attribute of the team instance.
    team.trophies_won = body_data.get('trophies_won')
    # Add the new team to the session and commit the changes to the database
    db.session.add(team)
    # Commit to add the team to the database
    db.session.commit()
        # Respond to the client
    # Serialize the created team using team_schema and return as a JSON response with a 201 status code.
    return team_schema.dump(team), 201

# Route to delete a specific team by its id
@teams_bp.route('/<int:id>', methods=['DELETE'])        # only admins can delete
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def delete_one_team(id):
    # Query the database to get the team with the specified id
    stmt = db.select(Team).filter_by(id=id)
    # Execute the query and return the result as a single team object.
    team = db.session.scalar(stmt)
    # if such a team exists, it will do the following:
    if team:
        # Delete the team from the database and commit the changes
        db.session.delete(team)
        db.session.commit()
        # returns message saying team deletion successful
        return { 'message': f'Team {team.team_name} deleted successfully!'}
    # if the team does not exist
    else:
        # Return an error response if the team with the specified id does not exist
        return { 'error': f'Team with id no.{id} does not exist and cannot be deleted!!!'}, 404
    
# Route to update a specific team by its id
@teams_bp.route('/<int:id>', methods=['PUT', 'PATCH'])           # only admins can edit or update
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def update_one_team(id):
    # Load the JSON request data into a team_schema object for validation. 
    # The partial=True argument indicates that the data is not required to include all fields, as it is a partial update.
    body_data = team_schema.load(request.get_json(), partial=True)
    # Query the database to get the team with the specified id
    stmt = db.select(Team).filter_by(id=id)
    # Execute the query and return the result as a single team object.
    team = db.session.scalar(stmt)
    # if the team exists
    if team:
        # Update the team with the new data from the request and commit the changes
        # Update the team attributes based on the data from the request using team.team_name = body_data.get('team_name') OR
        # if the data in the field is not provided, the existing value in the database remains unchanged.
        team.team_name = body_data.get('team_name') or team.team_name
        # Update the team attributes based on the data from the request using team.trophies_won = body_data.get('trophies_won') OR
        # if the data in the field is not provided, the existing value in the database remains unchanged.
        team.trophies_won = body_data.get('trophies_won') or team.trophies_won
        db.session.commit()
        # Serialize the updated team using team_schema and return as a JSON response.
        return team_schema.dump(team)
    # if the team does not exist
    else:
        # Return an error response if the team with the specified id does not exist
        return { 'error': f'The team with id no.{id} does not exist and cannot be updated!'}, 404