from flask import Blueprint, request
from init import db
from models.team_thread import Team_thread, team_thread_schema, team_threads_schema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp
from models.team import Team, team_schema, teams_schema
from models.user import User
from models.stadium import Stadium, stadium_schema, stadiums_schema
from controllers.team_thread_controller import authorise_as_admin


stadiums_bp = Blueprint('stadiums', __name__, url_prefix='/stadiums')

@stadiums_bp.route('/')
def get_all_stadiums():
    stmt = db.select(Stadium).order_by(Stadium.id.desc())
    stadiums = db.session.scalars(stmt)
    return stadiums_schema.dump(stadiums)

@stadiums_bp.route('/<int:id>')
def get_one_stadium(id):
    stmt = db.select(Stadium).filter_by(id=id)
    stadium = db.session.scalar(stmt)
    if stadium:
        return stadium_schema.dump(stadium)
    else:
        return { 'error': f'There is no existing stadium with id no.{id}!'}, 404

@stadiums_bp.route('/', methods=['POST'])    
@jwt_required()
def create_stadium():
    body_data = stadium_schema.load(request.get_json())

    # Create a new Stadium model instance from the stadium info
    stadium = Stadium() # Instance of the Stadium class which is in turn a SQLAlchemy model
    stadium.stadium_name = body_data.get('stadium_name')
    stadium.location = body_data.get('location')
    stadium.year_built = body_data.get('year_built')
    stadium.team_id = body_data.get('team_id')
    # Add the stadium to the session
    db.session.add(stadium)
    # Commit to add the stadium to the database
    db.session.commit()
        # Respond to the client
    return stadium_schema.dump(stadium), 201

@stadiums_bp.route('/<int:id>', methods=['DELETE'])        # only admins can delete
@jwt_required()
@authorise_as_admin
def delete_one_stadium(id):
    stmt = db.select(Stadium).filter_by(id=id)
    stadium = db.session.scalar(stmt)

    if stadium:
        db.session.delete(stadium)
        db.session.commit()
        return { 'message': f'Stadium {stadium.stadium_name} deleted successfully!'}
    else:
        return { 'error': f'Stadium with id no.{id} does not exist and cannot be deleted!!!'}, 404
    
    
@stadiums_bp.route('/<int:id>', methods=['PUT', 'PATCH'])           # only admins can edit or update
@jwt_required()
@authorise_as_admin
def update_one_stadium(id):
    body_data = stadium_schema.load(request.get_json(), partial=True)
    stmt = db.select(Stadium).filter_by(id=id)
    stadium = db.session.scalar(stmt)

    if stadium:
        stadium.stadium_name = body_data.get('stadium_name') or stadium.stadium_name
        stadium.location = body_data.get('location') or stadium.location
        stadium.year_built = body_data.get('year_built') or stadium.year_built
        stadium.team_id = body_data.get('team_id') or stadium.team_id

        db.session.commit()
        return stadium_schema.dump(stadium)
    else:
        return { 'error': f'The stadium with id no.{id} does not exist and cannot be updated!'}, 404