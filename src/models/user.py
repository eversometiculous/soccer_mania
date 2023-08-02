from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

# This is the User model. It represents the users table in the database. 
# It has various attributes like id, name, email, username, password, is_admin, and favourite_player. 
# The team_id attribute is a foreign key referencing the id column of the teams table.
# It establishes relationships with other tables, such as team_threads, team, and comments, through the db.relationship() method.
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    favourite_player = db.Column(db.String)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

    team_threads = db.relationship('Team_thread', back_populates='user', cascade='all, delete-orphan')
    team = db.relationship('Team', back_populates='users')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')

# This Marshmallow schema defines how the User model should be serialized (to JSON) and deserialized (from JSON).
# It uses the fields module to specify which attributes of the User model should be included in the serialization.
# The team_threads, team, and comments attributes are nested fields that use other 
# schemas (Team_threadSchema and CommentSchema) to format their serialization.
# The email and password fields have length validation rules using the Length class from marshmallow.validate 
# to ensure minimum lengths are met.

class UserSchema(ma.Schema):

    team_threads = fields.List(fields.Nested('Team_threadSchema', only=['title', 'date']))
    team = fields.Nested('TeamSchema', only=['team_name'])
    comments = fields.List(fields.Nested('CommentSchema', only=['id', 'date', 'message']))

    email = fields.String(validate=(Length(min=5, error='Email must be at least 5 characters long!')))
    password = fields.String(validate=(Length(min=6, error='Password must be at least 6 characters long!')))

    class Meta:
        fields = ('id', 'name', 'username', 'email', 'password', 'favourite_player', 'is_admin', 'team', 'team_threads', 'comments')
        ordered = True

# user_schema is an instance of UserSchema, configured to exclude the password field from serialization. 
# This is done for security reasons so that the password is not exposed in JSON responses.  
user_schema = UserSchema(exclude=['password'])
# users_schema is also an instance of UserSchema, but it is configured to handle lists of users, so it 
# includes multiple users and excludes their passwords.
users_schema = UserSchema(many=True, exclude=['password'])
