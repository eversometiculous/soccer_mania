from flask import Blueprint
from init import db
from models.user import User, user_schema, users_schema

# creates a blueprint called users_bp that has the url_prefix='/users'
users_bp = Blueprint('users', __name__, url_prefix='/users')

# Route to get all user details
@users_bp.route('/')
def get_all_users():
    # This query retrieves all users from the database and 
    # orders them in descending order based on their id
    stmt = db.select(User).order_by(User.id.desc())
   # Execute the query and return the results as a list of 
   # user objects using db.session.scalars().
    # The users_schema.dump(users) function serializes the list of 
    # user objects to JSON format.
    # It applies the serialization rules defined in the user_schema, 
    # excluding the 'password' field.
    users = db.session.scalars(stmt)
    return users_schema.dump(users)

# Route to get one specific user detail
@users_bp.route('/<int:id>')
def get_one_user(id):
    # This query retrieves a single user from the database based on the provided user id.
    stmt = db.select(User).filter_by(id=id)
    # Execute the query and return the result as a single user object using db.session.scalar().
    # The user_schema.dump(user) function serializes the user object to JSON format.
    # It applies the serialization rules defined in the user_schema, excluding the 'password' field.
    user = db.session.scalar(stmt)

    # Check if the user was found in the database. If found, return the serialized user data.
    # If not found, return an error message with a 404 status code.
    if user:
        return user_schema.dump(user)
    else:
        return { 'error': f'There is no existing user with id no.{id}!'}, 404