from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And

class Player(db.Model):
	__tablename__ = 'players'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	date_of_birth = db.Column(db.Text)
	position = db.Column(db.String)
	contract_period = db.Column(db.Text)
	current_salary = db.Column(db.Text)

	team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

	team = db.relationship('Team', back_populates='players') 

class PlayerSchema(ma.Schema):
	team = fields.Nested('TeamSchema', only=['team_name'])

	position =  fields.String(validate=(Length(min=2, error='Postion must be at least 2 characters long!')))
	contract_period = fields.String(required=True, validate=(Regexp('^[a-zA-Z0-9 -/]+$', error='Only numbers, spaces, letters, - and / are allowed')))
	date_of_birth = fields.String(required=True, validate=And(
	    Length(min=4, error='The date of birth must be at least 4 characters long!'),
		Regexp('^[a-zA-Z0-9 -/]+$', error='Only numbers, spaces, letters, - and / are allowed')
    ))

	class Meta:
		fields = ('id', 'name', 'date_of_birth', 'position', 'team_id', 'contract_period', 'current_salary', 'team')
		ordered = True

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)