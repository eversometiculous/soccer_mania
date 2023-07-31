from init import db, ma
from marshmallow import fields

class Player(db.Model):
	__tablename__ = 'players'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	date_of_birth = db.Column(db.Date)
	position = db.Column(db.String)
	contract_period = db.Column(db.Text)
	current_salary = db.Column(db.Text)

	team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

	team = db.relationship('Team', back_populates='players') 

class PlayerSchema(ma.Schema):
	team = fields.Nested('TeamSchema', only=['team_name'])

	class Meta:
		fields = ('id', 'name', 'date_of_birth', 'contract_period', 'current_salary', 'team')
		ordered = True

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)