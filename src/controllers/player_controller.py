from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp
from models.team import Team, team_schema, teams_schema
from models.user import User
from models.player import Player, player_schema, players_schema
from controllers.team_thread_controller import authorise_as_admin

# Create a Blueprint for handling players
players_bp = Blueprint('players', __name__, url_prefix='/players')

# Route to get all players
@players_bp.route('/')
def get_all_players():
    # Query the database to get all players and order them in descending order based on their id.
    stmt = db.select(Player).order_by(Player.id.desc())
    # Execute the query and return the results as a list of player objects.
    players = db.session.scalars(stmt)
    # Serialize the list of player objects using players_schema and return as a JSON response.
    return players_schema.dump(players)

# Route to get a specific player by its id
@players_bp.route('/<int:id>')
def get_one_player(id):
    # Query the database to get a player with the specified id.
    stmt = db.select(Player).filter_by(id=id)
    # Execute the query and return the result as a single player object.
    player = db.session.scalar(stmt)
    # Check if the player exists; if yes, serialize it using player_schema and return as a JSON response.
    # If not found, return an error response with a 404 status code.
    if player:
        return player_schema.dump(player)
    else:
        return { 'error': f'There is no existing player with id no.{id}!'}, 404

# Route to create a new player
@players_bp.route('/', methods=['POST'])
# Require a valid JWT token to access this route
@jwt_required()
def create_player():
    # Load the JSON request data into a player_schema object for validation.
    body_data = player_schema.load(request.get_json())

    # Create a new Player model instance and set its attributes based on the provided data from the request.
    # A new instance of the Player model is created, and its attributes (name, date_of_birth, position, contract_period, 
    # current_salary, and team_id) are set based on the validated JSON request data (body_data). 
    # It uses body_data.get() to retrieve the values from body_data and assign them to the corresponding player attributes.
    player = Player() # Instance of the Player class which is in turn a SQLAlchemy model
    player.name = body_data.get('name')
    player.date_of_birth = body_data.get('date_of_birth')
    player.position = body_data.get('position')
    player.contract_period = body_data.get('contract_period')
    player.current_salary = body_data.get('current_salary')
    player.team_id = body_data.get('team_id')
    # Add the new player to the session and commit the changes to the database.
    db.session.add(player)
    # Commit to add the player to the database
    db.session.commit()
    # Serialize the created player using player_schema and return as a JSON response with a 201 status code.
    return player_schema.dump(player), 201

# Route to delete a specific player by its id
@players_bp.route('/<int:id>', methods=['DELETE'])        # only admins can delete
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def delete_one_player(id):
    # Query the database to get the player with the specified id.
    stmt = db.select(Player).filter_by(id=id)
    # Execute the query and return the result as a single player object.
    player = db.session.scalar(stmt)
    # if player exists
    if player:
        # Delete the player from the database and commit the changes.
        db.session.delete(player)
        db.session.commit()
        # Return a message stating succcessful player deletion
        return { 'message': f'Player {player.name} deleted successfully!'}
    # if player does not exist
    else:
        # Return an error response if the player with the specified id does not exist.
        return { 'error': f'Player with id no.{id} does not exist and cannot be deleted!!!'}, 404

# Route to update a specific player by its id
@players_bp.route('/<int:id>', methods=['PUT', 'PATCH'])           # only admins can edit or update
# Require a valid JWT token to access this route
@jwt_required()
# Only admins can access this route and this decorator has extra code in it as seen in controllers.team_thread_controllers that help
# to get the user_id from the JWT token, query the database to get the user object, 
# check if the user is an admin, if yes, execute the decorated function; otherwise, return an error response saying only admins allowed.
@authorise_as_admin
def update_one_player(id):
    # Load the JSON request data into a player_schema object for validation.
    # The partial=True argument indicates that the data is not required to include all fields, as it is a partial update.
    body_data = player_schema.load(request.get_json(), partial=True)
    # Query the database to get the player with the specified id.
    stmt = db.select(Player).filter_by(id=id)
    # Execute the query and return the result as a single player object.
    player = db.session.scalar(stmt)

    if player:
        # Update the player with the new data from the request and commit the changes.
        # If the player exists, the route updates its attributes (name, date_of_birth, position, contract_period, 
        # current_salary, and team_id) based on the new data from the request (body_data). It uses body_data.get() to retrieve 
        # the values from body_data and update the player attributes. If a field is not provided in the request 
        # data (None or missing), it keeps the existing value for that field. This is done by using OR.
        player.name = body_data.get('name') or player.name
        player.date_of_birth = body_data.get('date_of_birth') or player.date_of_birth
        player.position = body_data.get('position') or player.position
        player.contract_period = body_data.get('contract_period') or player.contract_period
        player.current_salary = body_data.get('current_salary') or player.current_salary
        player.team_id = body_data.get('team_id') or player.team_id
        # commit the updated fields
        db.session.commit()
        # Serialize the updated player using player_schema and return as a JSON response.
        return player_schema.dump(player)
    else:
        # Return an error response if the player with the specified id does not exist.
        return { 'error': f'The player with id no.{id} does not exist and cannot be updated!'}, 404