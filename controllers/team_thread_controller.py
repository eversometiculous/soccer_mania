from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema



team_threads_bp = Blueprint('team_threads', __name__, url_prefix='/team_threads')

@team_threads_bp.route('/')
def get_all_team_threads():
    stmt = db.select(Team_thread).order_by(Team_thread.date.desc())
    team_threads = db.session.scalars(stmt)
    return team_threads_schema.dump(team_threads)