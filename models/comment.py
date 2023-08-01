from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

# The Comment model represents the 'comments' table in the database.
# It has attributes such as id, message, and date.
# There are two foreign key relationships: one with the Team_thread model through the team_thread_id column, 
# representing the team thread to which the comment belongs, and another with the User model through the user_id column, 
# representing the user who made the comment.
# The user and team_thread attributes represent the relationships with the User and Team_thread models, respectively.
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    date = db.Column(db.Date)

    team_thread_id = db.Column(db.Integer, db.ForeignKey('team_threads.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='comments', cascade='all, delete')
    team_thread = db.relationship('Team_thread', back_populates='comments', cascade='all, delete')

# The CommentSchema is a Marshmallow schema for serializing and deserializing the Comment model.
# The schema defines the fields that will be included in the serialized JSON response and parsed during deserialization.
# Nested fields (user and team_thread) are used to handle the relationships with the User and Team_thread models, respectively.
# The message field has a validation rule using the Length class from the marshmallow.validate module to ensure 
# it meets specific criteria.
class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username', 'id', 'favourite_player', 'is_admin'])
    team_thread = fields.Nested('Team_threadSchema', only=['id', 'title', 'description', 'date', 'user'])

    message = fields.String(required=True, validate=(
        Length(min=2, error='Message must be at least 2 characters long!')
    ))

    class Meta:
        fields = ('id', 'team_thread', 'user', 'date', 'message')
        ordered = True

# comment_schema is an instance of CommentSchema, used to serialize or deserialize a single comment object (one comment).
comment_schema = CommentSchema()
# comments_schema is an instance of CommentSchema, used to serialize or deserialize a list of comment objects (multiple comments).
comments_schema = CommentSchema(many=True)