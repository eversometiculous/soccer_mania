from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from models.comment import Comment, comment_schema, comments_schema
from datetime import date
from models.user import User, user_schema, users_schema

# Create a Blueprint for handling comments, which are tied into controllers.team_thread_controller parent blueprint and url_prefix
# creating a url prefix after the parent blueprint and the prefix in this blueprint indicated below.
comments_bp = Blueprint('comments', __name__, url_prefix='/<int:team_thread_id>/comments')

# /team_threads/comments

# /team_thread/team_thread_id/comments - POST

# Route to create a new comment on a specific team thread
@comments_bp.route('/', methods=['POST'])
# Require a valid JWT token to access this route
@jwt_required()
def create_comment(team_thread_id):
    # Load the JSON request data into a comment_schema object for validation.
    body_data = comment_schema.load(request.get_json())
    # Query the database to get the team thread with the specified team_thread_id.
    stmt = db.select(Team_thread).filter_by(id=team_thread_id) # select * from team_threads where id = team_thread_id
    # Execute the query and return the result as a single team thread object.
    team_thread = db.session.scalar(stmt)
    # Check if the team thread exists; if yes, create a new comment and associate it with the team thread.
    # if team_thread id exists 
    if team_thread:
        # create a new comment model
        comment = Comment(
            # Take the message from the JSON input and store it in the comment object.
            message = body_data.get('message'),
            # Puts the date as today's date as when the comment is posted!
            date=date.today(),
            # grabs the user_id from the get_jwt_identity token and stores it in the comment so people will know who made the comment!
            user_id=get_jwt_identity(),
            # Associate the comment with the specific team thread by setting its team_thread_id to the team_thread's id.
            team_thread_id=team_thread.id # or team_thread=team_thread
        )
       # Add the comment to the session and commit the changes to the database.
        db.session.add(comment)
        db.session.commit()
        # Serialize the created comment using comment_schema and return as a JSON response with a 201 status code.
        return comment_schema.dump(comment), 201
    # if team_thread id does not exist
    else:
        # if thread does not exist, error pop ups saying team thread with specific id does not exist, with a 404 status code.
        return { 'error': f'Team_thread with id no.{id} does not exist and cannot be commented on!'}, 404

# Route to delete a specific comment on a team thread
@comments_bp.route('<int:comment_id>', methods=['DELETE'])
# Require a valid JWT token to access this route
@jwt_required()
def delete_comment(team_thread_id, comment_id):
    # Get the user id from the JWT token and fetch the corresponding user from the database.
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    # Query the database to get the comment with the specified comment_id.
    stmt = db.select(Comment).filter_by(id=comment_id)
    # Execute the query and return the result as a single comment object.
    comment = db.session.scalar(stmt)
    # if comment exists
    if comment:
        # Check if the user is the creator of the comment or an admin. If yes, delete the comment and commit the changes.
        if str(comment.user_id) == user_id or user.is_admin:
            db.session.delete(comment)
            db.session.commit()
            return { 'message': f'Comment {comment.message} deleted successfully!'}
        # if user trying to delete is not the creator of comment or an admin
        else:
            # Return an error response with a 403 status code indicating forbidden access.
            return { 'error': 'Only the admin or the user who created the comment can delete it!! Sorry!!'}, 403
    # if comment does not exist
    else:
        # Return an error response with a 404 status code if the comment with the specified id does not exist.
        return { 'error': f'Comment with id no.{comment_id} does not exist'}, 404

# Route to update a specific comment on a team thread
@comments_bp.route('/<int:comment_id>', methods=['PUT', 'PATCH'])
# Require a valid JWT token to access this route
@jwt_required()
def update_comment(team_thread_id, comment_id):
    # Load the JSON request data into a comment_schema object for validation.
    # The partial=True argument indicates that the data is not required to include all fields, as it is a partial update.
    body_data = comment_schema.load(request.get_json(), partial=True)
    # Query the database to get the comment with the specified comment_id.
    stmt = db.select(Comment).filter_by(id=comment_id)
    # Execute the query and return the result as a single comment object.
    comment = db.session.scalar(stmt)
    # Get the user id from the JWT token and fetch the corresponding user from the database.
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    # if comment exists
    if comment:
        # Check if the user is the creator of the comment or an admin. If yes, update the comment and commit the changes.
        if str(comment.user_id) == user_id or user.is_admin:
            comment.message = body_data.get('message') or comment.message
            # commit the changes to the comment table in the database
            db.session.commit()
            # Serialize the updated comment using comment_schema and return as a JSON response.
            return comment_schema.dump(comment)
        # if user trying to update comment is not the creator or an admin
        else:
            # Return an error response with a 403 status code indicating forbidden access.
            return { 'error': 'Only the admin or the user who created the comment can update or edit it!! Sorry!!'}, 403
    # if comment does not exist
    else:
        # Return an error response with a 404 status code if the comment with the specified id does not exist.
        return { 'error': f'Comment with id no.{comment_id} does not exist and cannot be editted'}, 404