from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp
from models.team import Team, team_schema, teams_schema
from models.user import User

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

@teams_bp.route('/')
def get_all_teams():
    stmt = db.select(Team).order_by(Team.id.desc())
    teams = db.session.scalars(stmt)
    return teams_schema.dump(teams)