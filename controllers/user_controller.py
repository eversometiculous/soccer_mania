from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp
from models.team import Team, team_schema, teams_schema
from models.user import User

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def get_all_users():
    stmt = db.select(User).order_by(User.id.desc())
    users = db.session.scalars(stmt)
    return users_schema.dump(users)

@users_bp.route('/<int:id>')
def get_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return user_schema.dump(user)
    else:
        return { 'error': f'There is no existing user with id no.{id}!'}, 404
