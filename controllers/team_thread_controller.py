from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp

team_threads_bp = Blueprint('team_threads', __name__, url_prefix='/team_threads')
team_threads_bp.register_blueprint(comments_bp)

@team_threads_bp.route('/')
def get_all_team_threads():
    stmt = db.select(Team_thread).order_by(Team_thread.id.desc())
    team_threads = db.session.scalars(stmt)
    return team_threads_schema.dump(team_threads)

@team_threads_bp.route('/<int:id>')
def get_one_team_thread(id):
    stmt = db.select(Team_thread).filter_by(id=id)
    team_thread = db.session.scalar(stmt)
    if team_thread:
        return team_thread_schema.dump(team_thread)
    else:
        return { 'error': f'There is no existing team thread with id no.{id}!'}, 404
    
@team_threads_bp.route('/', methods=['POST'])
@jwt_required()
def create_team_thread():
    body_data = request.get_json()
    # create a new Team thread model instance
    team_thread = Team_thread(
        title=body_data.get('title'),
        description=body_data.get('description'),
        date=date.today(),
        user_id=get_jwt_identity(),
        team_id=get_jwt_identity()
    )
    # Add that team_thread to the session
    db.session.add(team_thread)
    # Commit
    db.session.commit()
    # Respond to the client
    return team_thread_schema.dump(team_thread), 201

@team_threads_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_team_thread(id):
    stmt = db.select(Team_thread).filter_by(id=id)
    team_thread = db.session.scalar(stmt)
    if team_thread:
        db.session.delete(team_thread)
        db.session.commit()
        return { 'message': f'Team thread {team_thread.title} deleted succesffuly!'}
    else:
        return { 'error': f'Team thread with id no.{id} does not exist and can not be deleted!'}, 404
    
@team_threads_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_team_thread(id):
    body_data = request.get_json()
    stmt = db.select(Team_thread).filter_by(id=id)
    team_thread = db.session.scalar(stmt)
    if team_thread:
        team_thread.title = body_data.get('title') or team_thread.title
        team_thread.description = body_data.get('description') or team_thread.description
        team_thread.date_updated = date.today()
        db.session.commit()
        return team_thread_schema.dump(team_thread)
    else:
        return { 'error': f'The team thread with id no.{id} does not exist and cannot be updated!'}, 404