from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.comment import Comment, comment_schema, comments_schema
from models.user import User, user_schema, users_schema


team_threads_bp = Blueprint('team_threads', __name__, url_prefix='/team_threads')

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
    

# /team_thread/team_thread_id/comments - POST

@team_threads_bp.route('/<int:team_thread_id>/comments', methods=['POST'])
@jwt_required()
def create_comment(team_thread_id):
    body_data = request.get_json()
    stmt = db.select(Team_thread).filter_by(id=team_thread_id) # select * from team_threads where id = team_thread_id
    team_thread = db.session.scalar(stmt)
    if team_thread:
        comment = Comment(
            message = body_data.get('message'),
            date=date.today(),
            user_id=get_jwt_identity(),
            team_thread_id=team_thread.id # or team_thread=team_thread
        )

        db.session.add(comment)
        db.session.commit()
        return comment_schema.dump(comment), 201
    else:
        return { 'error': f'Team_thread with id no.{id} does not exist and cannot be commented on!'}, 404
    
@team_threads_bp.route('/<int:team_thread_id>/comments/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(team_thread_id, comment_id):
    stmt = db.select(Comment).filter_by(id=comment_id)
    comment = db.session.scalar(stmt)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return { 'message': f'Comment {comment.message} deleted successfully!'}
    else:
        return { 'error': f'Comment with id no.{comment_id} does not exist'}, 404
    
@team_threads_bp.route('/<int:team_thread_id>/comments/<int:comment_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_comment(team_thread_id, comment_id):
    body_data = request.get_json()
    stmt = db.select(Comment).filter_by(id=comment_id)
    comment = db.session.scalar(stmt)
    if comment:
        comment.message = body_data.get('message') or comment.message
        db.session.commit()
        return comment_schema.dump(comment)
    else:
        return { 'error': f'Comment with id no.{comment_id} does not exist and cannot be editted'}, 404
