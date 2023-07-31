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

players_bp = Blueprint('players', __name__, url_prefix='/players')

@players_bp.route('/')
def get_all_players():
    stmt = db.select(Player).order_by(Player.id.desc())
    players = db.session.scalars(stmt)
    return players_schema.dump(players)

@players_bp.route('/<int:id>')
def get_one_player(id):
    stmt = db.select(Player).filter_by(id=id)
    player = db.session.scalar(stmt)
    if player:
        return player_schema.dump(player)
    else:
        return { 'error': f'There is no existing player with id no.{id}!'}, 404
    
@players_bp.route('/', methods=['POST'])
@jwt_required()
def create_player():
    body_data = player_schema.load(request.get_json())

    # Create a new Player model instance from the player info
    player = Player() # Instance of the Player class which is in turn a SQLAlchemy model
    player.name = body_data.get('name')
    player.date_of_birth = body_data.get('date_of_birth')
    player.position = body_data.get('position')
    player.contract_period = body_data.get('contract_period')
    player.current_salary = body_data.get('current_salary')
    player.team_id = body_data.get('team_id')
    # Add the player to the session
    db.session.add(player)
    # Commit to add the player to the database
    db.session.commit()
        # Respond to the client
    return player_schema.dump(player), 201

@players_bp.route('/<int:id>', methods=['DELETE'])        # only admins can delete
@jwt_required()
@authorise_as_admin
def delete_one_player(id):
    stmt = db.select(Player).filter_by(id=id)
    player = db.session.scalar(stmt)

    if player:
        db.session.delete(player)
        db.session.commit()
        return { 'message': f'Player {player.name} deleted successfully!'}
    else:
        return { 'error': f'Player with id no.{id} does not exist and cannot be deleted!!!'}, 404
    
@players_bp.route('/<int:id>', methods=['PUT', 'PATCH'])           # only admins can edit or update
@jwt_required()
@authorise_as_admin
def update_one_player(id):
    body_data = player_schema.load(request.get_json(), partial=True)
    stmt = db.select(Player).filter_by(id=id)
    player = db.session.scalar(stmt)

    if player:
        player.name = body_data.get('name') or player.name
        player.date_of_birth = body_data.get('date_of_birth') or player.date_of_birth
        player.position = body_data.get('position') or player.position
        player.contract_period = body_data.get('contract_period') or player.contract_period
        player.current_salary = body_data.get('current_salary') or player.current_salary
        player.team_id = body_data.get('team_id') or player.team_id

        db.session.commit()
        return player_schema.dump(player)
    else:
        return { 'error': f'The player with id no.{id} does not exist and cannot be updated!'}, 404