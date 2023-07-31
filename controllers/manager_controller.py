from flask import Blueprint, request
from init import db
from models.team_thread import team_thread_schema, team_threads_schema
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User, user_schema, users_schema
from controllers.comment_controller import comments_bp
from models.team import Team, team_schema, teams_schema
from models.user import User
from models.manager import Manager, manager_schema, managers_schema
from controllers.team_thread_controller import authorise_as_admin

managers_bp = Blueprint('managers', __name__, url_prefix='/managers')

@managers_bp.route('/')
def get_all_managers():
    stmt = db.select(Manager).order_by(Manager.id.desc())
    managers = db.session.scalars(stmt)
    return managers_schema.dump(managers)

@managers_bp.route('/<int:id>')
def get_one_manager(id):
    stmt = db.select(Manager).filter_by(id=id)
    manager = db.session.scalar(stmt)
    if manager:
        return manager_schema.dump(manager)
    else:
        return { 'error': f'There is no existing manager with id no.{id}!'}, 404
    
@managers_bp.route('/', methods=['POST'])
@jwt_required()
def create_manager():
    body_data = manager_schema.load(request.get_json())

    # Create a new Manager model instance from the manager info
    manager = Manager() # Instance of the Manager class which is in turn a SQLAlchemy model
    manager.name = body_data.get('name')
    manager.date_of_birth = body_data.get('date_of_birth')
    manager.teams_managed_previously = body_data.get('teams_managed_previously')
    manager.trophies_won = body_data.get('trophies_won')
    manager.team_id = body_data.get('team_id')
    # Add the manager to the session
    db.session.add(manager)
    # Commit to add the manager to the database
    db.session.commit()
        # Respond to the client
    return manager_schema.dump(manager), 201

@managers_bp.route('/<int:id>', methods=['DELETE'])        # only admins can delete
@jwt_required()
@authorise_as_admin
def delete_one_manager(id):
    stmt = db.select(Manager).filter_by(id=id)
    manager = db.session.scalar(stmt)

    if manager:
        db.session.delete(manager)
        db.session.commit()
        return { 'message': f'Manager {manager.name} deleted successfully!'}
    else:
        return { 'error': f'Manager with id no.{id} does not exist and cannot be deleted!!!'}, 404
    
@managers_bp.route('/<int:id>', methods=['PUT', 'PATCH'])           # only admins can edit or update
@jwt_required()
@authorise_as_admin
def update_one_manager(id):
    body_data = manager_schema.load(request.get_json(), partial=True)
    stmt = db.select(Manager).filter_by(id=id)
    manager = db.session.scalar(stmt)

    if manager:
        manager.name = body_data.get('name') or manager.name
        manager.date_of_birth = body_data.get('date_of_birth') or manager.date_of_birth
        manager.teams_managed_previously = body_data.get('teams_managed_previously') or manager.teams_managed_previously
        manager.trophies_won = body_data.get('trophies_won') or manager.trophies_won
        manager.team_id = body_data.get('team_id') or manager.team_id

        db.session.commit()
        return manager_schema.dump(manager)
    else:
        return { 'error': f'The manager with id no.{id} does not exist and cannot be updated!'}, 404