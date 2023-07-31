from init import db, ma
from marshmallow import fields

class Stadium(db.Model):
	__tablename__ = 'stadiums'

	id = db.Column(db.Integer, primary_key=True)
	stadium_name = db.Column(db.String)
	location = db.Column(db.String)
	year_built = db.Column(db.Integer)

	team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

	team = db.relationship('Team', back_populates='stadium')

class StadiumSchema(ma.Schema):
	team = fields.Nested('TeamSchema', only=['team_name'])

	class Meta:
		fields = ('id', 'stadium_name', 'location', 'year_built', 'team')
		ordered = True

stadium_schema = StadiumSchema()
stadiums_schema = StadiumSchema(many=True)