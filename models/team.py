from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

# The Team model represents the 'teams' table in the database.
# It has attributes such as id, team_name, and trophies_won.
# There are various relationships defined using db.relationship to connect Team with other related models like Manager, 
# Stadium, Player, Team_thread, and User.
# These relationships define how data from other tables is linked to the Team model.
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

# The TeamSchema is a Marshmallow schema for serializing and deserializing the Team model.
# The schema defines the fields that will be included in the serialized JSON response and parsed during deserialization.
# Nested fields are used to handle relationships with other models, such as users, team_threads, manager, stadium, and players.
# The team_name field has a validation rule that ensures the team name is at least 2 characters long.
class TeamSchema(ma.Schema):
    users = fields.List(fields.Nested('UserSchema', only=['username', 'id', 'favourite_player', 'is_admin']))
    team_threads = fields.List(fields.Nested('Team_threadSchema', only=['title', 'date', 'user']))
    manager = fields.Nested('ManagerSchema', only=['name'])
    stadium = fields.List(fields.Nested('StadiumSchema', only=['stadium_name']))
    players = fields.List(fields.Nested('PlayerSchema', only=['name']))

    team_name = fields.String(validate=(Length(min=2, error='Team name must be at least 2 characters long!')))

    class Meta:
        fields = ('id', 'team_name', 'trophies_won', 'manager', 'stadium', 'players', 'users', 'team_threads')
        ordered = True

# team_schema is an instance of TeamSchema, used to serialize or deserialize a single team object (one team).
team_schema=TeamSchema()
# teams_schema is an instance of TeamSchema, used to serialize or deserialize a list of team objects (multiple teams).
teams_schema=TeamSchema(many=True)
