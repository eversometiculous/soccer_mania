from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And

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

	stadium_name =  fields.String(validate=(Length(min=2, error='Stadium name must be at least 2 characters long!')))
	location =  fields.String(validate=(Length(min=2, error='Location must be at least 2 characters long!')))
	year_built = fields.String(required=True, validate=And(
	    Length(min=2, error='The year built must be at least 2 characters long!'),
		Regexp('^[0-9]+$', error='Only numbers are allowed')
    ))


	class Meta:
		fields = ('id', 'stadium_name',  'team_id', 'location', 'year_built', 'team')
		ordered = True

stadium_schema = StadiumSchema()
stadiums_schema = StadiumSchema(many=True)