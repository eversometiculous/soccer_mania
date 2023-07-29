from init import db, ma
from marshmallow import fields

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, unique=True, nullable=False)
    trophies_won = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    team_threads = db.relationship('Team_thread', back_populates='team', cascade='all, delete')
    user = db.relationship('User', back_populates='team')

class TeamSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username', 'id'])
    team_threads = fields.List(fields.Nested('Team_threadSchema', only=['title', 'date']))

    class Meta:
        fields = ('id', 'team_name', 'trophies_won', 'user', 'team_threads')
        ordered = True

team_schema=TeamSchema()
teams_schema=TeamSchema(many=True)
