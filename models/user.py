from init import db, ma
from marshmallow import fields


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    favourite_player = db.Column(db.String)

    team_threads = db.relationship('Team_thread', back_populates='user', cascade='all, delete')
    team = db.relationship('Team', back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):

    team_threads = fields.List(fields.Nested('Team_threadSchema', only=['title', 'date']))
    team = fields.Nested('TeamSchema', only=['team_name'])

    class Meta:
        fields = ('id', 'name', 'username', 'email', 'password', 'favourite_player', 'is_admin', 'team', 'team_threads')
        ordered = True
        
user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])
