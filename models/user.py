from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length


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

class UserSchema(ma.Schema):

    team_threads = fields.List(fields.Nested('Team_threadSchema', only=['title', 'date']))
    team = fields.Nested('TeamSchema', only=['team_name'])
    comments = fields.List(fields.Nested('CommentSchema', only=['id', 'date', 'message']))

    email = fields.String(validate=Length(min=5, error='Title must be at least 5 characters long!'))   
    password = fields.String(validate=Length(min=6, error='Password must be at least 6 characters long!'))

    class Meta:
        fields = ('id', 'name', 'username', 'email', 'password', 'favourite_player', 'is_admin', 'team', 'team_threads', 'comments')
        ordered = True
        
user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])
