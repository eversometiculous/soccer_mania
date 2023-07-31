from init import db, ma
from marshmallow import fields

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

	class Meta:
		fields = ('id', 'name', 'date_of_birth', 'teams_managed_previously', 'team_id', 'trophies_won', 'team')
		ordered = True

manager_schema = ManagerSchema()
managers_schema = ManagerSchema(many=True)