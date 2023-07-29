from init import db, ma
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    date = db.Column(db.Date)

    team_thread_id = db.Column(db.Integer, db.ForeignKey('team_threads.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='comments')
    team_thread = db.relationship('Team_thread', back_populates='comments')

class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username', 'id', 'favourite_player'])
    team_thread = fields.Nested('Team_threadSchema', only=['id', 'title', 'description', 'date'])

    class Meta:
        fields = ('id', 'user', 'team_thread', 'date', 'message')
        ordered = True

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)