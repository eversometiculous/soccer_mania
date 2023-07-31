from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And

class Manager(db.Model):
	__tablename__ = 'managers'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	date_of_birth = db.Column(db.Text)
	teams_managed_previously = db.Column(db.Text)
	trophies_won = db.Column(db.Text)

	team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

	team = db.relationship('Team', back_populates='manager') 

class ManagerSchema(ma.Schema):
	team = fields.Nested('TeamSchema', only=['team_name'])

	date_of_birth = fields.String(required=True, validate=And(
	    Length(min=4, error='The date of birth must be at least 4 characters long!'),
		Regexp('^[a-zA-Z0-9 -/]+$', error='Only numbers, spaces, letters, - and / are allowed')
    ))

	class Meta:
		fields = ('id', 'name', 'date_of_birth', 'teams_managed_previously', 'team_id', 'trophies_won', 'team')
		ordered = True

manager_schema = ManagerSchema()
managers_schema = ManagerSchema(many=True)