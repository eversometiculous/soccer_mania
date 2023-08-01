from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And

# The Stadium model represents the 'stadiums' table in the database.
# It has attributes such as id, stadium_name, location, and year_built.
# There is a foreign key relationship with the Team model through the team_id column, representing the team that the stadium is associated with.
# The team attribute represents the relationship with the Team model.
class Stadium(db.Model):
	__tablename__ = 'stadiums'

	id = db.Column(db.Integer, primary_key=True)
	stadium_name = db.Column(db.String)
	location = db.Column(db.String)
	year_built = db.Column(db.Integer)

	team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

	team = db.relationship('Team', back_populates='stadium')

# The StadiumSchema is a Marshmallow schema for serializing and deserializing the Stadium model.
# The schema defines the fields that will be included in the serialized JSON response and parsed during deserialization.
# Nested fields are used to handle the relationship with the team.
# The stadium_name and location fields have validation rules using the Length class from marshmallow.validate 
# module to ensure they have a minimum length of 2 characters.
# The year_built field has validation rules using the And class from marshmallow.validate module to ensure 
# it has a minimum length of 2 characters and consists of only numbers.
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

# stadium_schema is an instance of StadiumSchema, used to serialize or deserialize a single stadium object (one stadium).
stadium_schema = StadiumSchema()
# stadiums_schema is an instance of StadiumSchema, used to serialize or deserialize a list of stadium objects (multiple stadiums).
stadiums_schema = StadiumSchema(many=True)