from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And


# The Player model represents the 'players' table in the database.
# It has attributes such as id, name, date_of_birth, position, contract_period, and current_salary.
# There is a foreign key relationship with the Team model through the team_id column, 
# representing the team that the player is associated with.
# The team attribute represents the relationship with the Team model.
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

# The PlayerSchema is a Marshmallow schema for serializing and deserializing the Player model.
# The schema defines the fields that will be included in the serialized JSON response and parsed during deserialization.
# Nested fields are used to handle the relationship with the team.
# The position, contract_period, and date_of_birth fields have validation rules using 
# the Length and Regexp classes from the marshmallow.validate module to ensure they meet specific criteria.
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

# player_schema is an instance of PlayerSchema, used to serialize or deserialize a single player object (one player).
player_schema = PlayerSchema()
# players_schema is an instance of PlayerSchema, used to serialize or deserialize a list of player objects (multiple players).
players_schema = PlayerSchema(many=True)