from init import db, ma
from marshmallow import fields

class Team_thread(db.Model):
    __tablename__ = 'team_threads'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date) # Date created
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

    user = db.relationship('User', back_populates='team_threads')         # the r in relationship is small
    team = db.relationship('Team', back_populates='teams')         # the r in relationship is small

class Team_threadSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    team = fields.Nested('TeamSchema', only=['user_id'])

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'user', 'team')
        ordered = True

team_thread_schema = Team_threadSchema()
team_threads_schema = Team_threadSchema(many=True)