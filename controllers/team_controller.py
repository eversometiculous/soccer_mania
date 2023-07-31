from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp
from models.team import Team, team_schema, teams_schema
from models.user import User
from controllers.team_thread_controller import authorise_as_admin

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

@teams_bp.route('/')
def get_all_teams():
    stmt = db.select(Team).order_by(Team.id.desc())
    teams = db.session.scalars(stmt)
    return teams_schema.dump(teams)

@teams_bp.route('/<int:id>')
def get_one_team(id):
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)
    if team:
        return team_schema.dump(team)
    else:
        return { 'error': f'There is no existing team with id no.{id}!'}, 404
    
@teams_bp.route('/', methods=['POST'])
@jwt_required()
def create_team():
    body_data = team_schema.load(request.get_json())

    # Create a new User model instance from the user info
    team = Team() # Instance of the User class which is in turn a SQLAlchemy model
    team.team_name = body_data.get('team_name')
    team.trophies_won = body_data.get('trophies_won')
    # Add the team to the session
    db.session.add(team)
    # Commit to add the team to the database
    db.session.commit()
        # Respond to the client
    return team_schema.dump(team), 201

@teams_bp.route('/<int:id>', methods=['DELETE'])        # only admins can delete
@jwt_required()
@authorise_as_admin
def delete_one_team(id):
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)

    if team:
        db.session.delete(team)
        db.session.commit()
        return { 'message': f'Team {team.team_name} deleted successfully!'}
    else:
        return { 'error': f'Team with id no.{id} does not exist and cannot be deleted!!!'}, 404
    
@teams_bp.route('/<int:id>', methods=['PUT', 'PATCH'])           # only admins can edit or update
@jwt_required()
@authorise_as_admin
def update_one_team(id):
    body_data = team_schema.load(request.get_json(), partial=True)
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)

    if team:
        team.team_name = body_data.get('team_name') or team.team_name
        team.trophies_won = body_data.get('trophies_won') or team.trophies_won
        db.session.commit()
        return team_schema.dump(team)
    else:
        return { 'error': f'The team with id no.{id} does not exist and cannot be updated!'}, 404