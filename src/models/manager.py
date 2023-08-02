from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And

# The Manager model represents the 'managers' table in the database.
# It has attributes such as id, name, date_of_birth, teams_managed_previously, and trophies_won.
# There is a foreign key relationship with the Team model through the team_id column, representing the team that the manager is associated with.
# The team attribute represents the relationship with the Team model.
class Manager(db.Model):
	__tablename__ = 'managers'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	date_of_birth = db.Column(db.Text)
	teams_managed_previously = db.Column(db.Text)
	trophies_won = db.Column(db.Text)

	team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

	team = db.relationship('Team', back_populates='manager') 

# The ManagerSchema is a Marshmallow schema for serializing and deserializing the Manager model.
# The schema defines the fields that will be included in the serialized JSON response and parsed during deserialization.
# Nested fields are used to handle the relationship with the team.
# The date_of_birth field has validation rules using the Length and Regexp classes from the 
# marshmallow.validate module to ensure it meets specific criteria.
class ManagerSchema(ma.Schema):
	team = fields.Nested('TeamSchema', only=['team_name'])

	date_of_birth = fields.String(required=True, validate=And(
	    Length(min=4, error='The date of birth must be at least 4 characters long!'),
		Regexp('^[a-zA-Z0-9 -/]+$', error='Only numbers, spaces, letters, - and / are allowed')
    ))

	class Meta:
		fields = ('id', 'name', 'date_of_birth', 'teams_managed_previously', 'team_id', 'trophies_won', 'team')
		ordered = True

# manager_schema is an instance of ManagerSchema, used to serialize or deserialize a single manager object (one manager).
manager_schema = ManagerSchema()
# managers_schema is an instance of ManagerSchema, used to serialize or deserialize a list of manager objects (multiple managers).
managers_schema = ManagerSchema(many=True)