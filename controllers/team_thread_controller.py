from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp
from models.team import Team, team_schema, teams_schema
from models.user import User

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
    body_data = team_thread_schema.load(request.get_json())  # team_thread_schema.load is required to do marshmallow validation(eg. 2 min characters).
    # Otherwise it will not bother with marshmallow min character length. If it just have body_data = request.get_json(), min characters wont matter.
    # create a new Team thread model instance
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify(message="User not found"), 404
    if not user.team:
        return jsonify(message="User's team not found"), 404

    team_thread = Team_thread(
        title=body_data.get('title'),
        description=body_data.get('description'),
        date=date.today(),
        user=user,
        team=user.team
    )
    # Add that team_thread to the session
    db.session.add(team_thread)
    # Commit
    db.session.commit()
    # Respond to the client
    return team_thread_schema.dump(team_thread), 201

@team_threads_bp.route('/<int:id>', methods=['DELETE']) # only admins can delete for now
@jwt_required()
def delete_one_team_thread(id):
    is_admin = authorise_as_admin()
    if not is_admin:
        return { 'error': 'Sorry, you are not authorised to delete this team thread!'}, 403
    stmt = db.select(Team_thread).filter_by(id=id)
    team_thread = db.session.scalar(stmt)
    if team_thread:
        db.session.delete(team_thread)
        db.session.commit()
        return { 'message': f'Team thread {team_thread.title} deleted succesffuly!'}
    else:
        return { 'error': f'Team thread with id no.{id} does not exist and can not be deleted!'}, 404
    
@team_threads_bp.route('/<int:id>', methods=['PUT', 'PATCH']) # only users who created the card can edit the card
@jwt_required()
def update_one_team_thread(id):
    body_data = team_thread_schema.load(request.get_json(), partial=True)
    stmt = db.select(Team_thread).filter_by(id=id)
    team_thread = db.session.scalar(stmt)
    if team_thread:
        if str(team_thread.user_id) != get_jwt_identity():
            return { 'error': 'Sorry! Only the person who created the team thread can edit the team thread!'}, 403
    if team_thread:
        team_thread.title = body_data.get('title') or team_thread.title
        team_thread.description = body_data.get('description') or team_thread.description
        team_thread.date_updated = date.today()
        db.session.commit()
        return team_thread_schema.dump(team_thread)
    else:
        return { 'error': f'The team thread with id no.{id} does not exist and cannot be updated!'}, 404
    
def authorise_as_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    return user.is_admin
