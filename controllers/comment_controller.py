from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from models.comment import Comment, comment_schema, comments_schema
from datetime import date

comments_bp = Blueprint('comments', __name__, url_prefix='/<int:team_thread_id>/comments')

# /team_threads/comments

# /team_thread/team_thread_id/comments - POST

@comments_bp.route('/', methods=['POST'])
@jwt_required()
def create_comment(team_thread_id):
    body_data = comment_schema.load(request.get_json())
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
    
@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
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
    
@comments_bp.route('/<int:comment_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_comment(team_thread_id, comment_id):
    body_data = comment_schema.load(request.get_json(), partial=True)
    stmt = db.select(Comment).filter_by(id=comment_id)
    comment = db.session.scalar(stmt)
    if comment:
        comment.message = body_data.get('message') or comment.message
        db.session.commit()
        return comment_schema.dump(comment)
    else:
        return { 'error': f'Comment with id no.{comment_id} does not exist and cannot be editted'}, 404
