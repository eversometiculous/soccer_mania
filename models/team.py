from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, unique=True, nullable=False)
    trophies_won = db.Column(db.Text)
    
    manager = db.relationship('Manager', back_populates='team', cascade='all, delete')
    stadium = db.relationship('Stadium', back_populates='team', cascade='all, delete')
    players = db.relationship('Player', back_populates='team', cascade='all, delete')
    team_threads = db.relationship('Team_thread', back_populates='team', cascade='all, delete')
    users = db.relationship('User', back_populates='team', cascade='all, delete-orphan')

class TeamSchema(ma.Schema):
    users = fields.List(fields.Nested('UserSchema', only=['username', 'id', 'favourite_player', 'is_admin']))
    team_threads = fields.List(fields.Nested('Team_threadSchema', only=['title', 'date', 'user']))
    manager = fields.Nested('ManagerSchema', only=['name'])
    stadium = fields.List(fields.Nested('StadiumSchema', only=['stadium_name']))
    players = fields.List(fields.Nested('PlayerSchema', only=['name']))

    team_name = fields.String(validate=(
        Length(min=2, error='Title must be at least 2 characters long!')
    ))

    class Meta:
        fields = ('id', 'team_name', 'trophies_won', 'manager', 'stadium', 'players', 'users', 'team_threads')
        ordered = True

team_schema=TeamSchema()
teams_schema=TeamSchema(many=True)
