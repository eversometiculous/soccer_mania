from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# To create a SQLAlchemy instance, which is used to interact with the database. SQLAlchemy has an ORM (Object-Relational Mapping) 
# interface to work with database models.
db = SQLAlchemy()

# To create a Marshmallow instance, which is a powerful library for object serialization/deserialization. Marshmallow will help 
# to convert complex data structures, like SQLAlchemy models, to JSON and vice versa.
ma = Marshmallow()

# To create a Bcrypt instance, which is used for password hashing and verification. It helps to enchance seucrity.
# It securely hashes passwords and then stores them in the database.
bcrypt = Bcrypt()

# To create a JWTManager instance, which is used for JSON Web Token (JWT) authentication and authorization. It is used to handle user 
# authentication by generating, verifying, and refreshing JWTs.
jwt = JWTManager()