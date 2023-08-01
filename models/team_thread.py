from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp


# The Team_thread model represents the 'team_threads' table in the database.
# It has attributes such as id, title, description, and date.
# There are foreign key relationships with the User and Team models through the user_id and team_id columns, respectively.
# Additionally, there is a relationship with the Comment model through the comments attribute.
# The relationships define how data from other tables is linked to the Team_thread model.
class Team_thread(db.Model):
    __tablename__ = 'team_threads'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    date = db.Column(db.Date) # Date created
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

    user = db.relationship('User', back_populates='team_threads', foreign_keys=[user_id])       # the r in relationship is small
    team = db.relationship('Team', back_populates='team_threads', foreign_keys=[team_id])         # the r in relationship is small
    comments = db.relationship('Comment', back_populates='team_thread', cascade='all, delete-orphan') 

# The Team_threadSchema is a Marshmallow schema for serializing and deserializing the Team_thread model.
# The schema defines the fields that will be included in the serialized JSON response and parsed during deserialization.
# Nested fields are used to handle relationships with other models, such as user, team, and comments.
# The title field has validation rules using the And class from marshmallow.validate module 
# to ensure it has a minimum length of 2 characters and consists of only letters, spaces, and numbers.
# The description field also has a validation rule to ensure it has a minimum length of 2 characters.
class Team_threadSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username', 'id', 'favourite_player', 'is_admin'])
    team = fields.Nested('TeamSchema', only=['team_name'])
    comments = fields.List(fields.Nested('CommentSchema', only=['id', 'date', 'message', 'user']))

    title = fields.String(required=True, validate=And(
        Length(min=2, error='Title must be at least 2 characters long!'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, spaces and numbers are allowed')
    ))

    description = fields.String(validate=(
        Length(min=2, error='Title must be at least 2 characters long!')
    ))

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'team_id', 'user', 'team', 'comments')
        ordered = True

# team_thread_schema is an instance of Team_threadSchema, 
# used to serialize or deserialize a single team thread object (one team thread).
team_thread_schema = Team_threadSchema()
# team_threads_schema is an instance of Team_threadSchema, used to serialize or 
# deserialize a list of team thread objects (multiple team threads).
team_threads_schema = Team_threadSchema(many=True) 