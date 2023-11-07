from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-posts.user',)

    id = db.Column(db.Integer, primary_key = True)
    email_address = db.Column(db.String, unique = True, nullable = False)
    username = db.Column(db.String, nullable = False)
    full_name = db.Column(db.String)
    _password_hash = db.Column(db.String)
    permission_level = db.Column(db.Integer)

    posts = db.relationship('Post', back_populates= 'user')
    # dashboard = db.relationship('Dashboard', back_populates= 'user')

    def __repr__(self):
        return f'<User {self.id}, {self.email_address}, {self.full_name}>'

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, new_pass):
        pass_hash = bcrypt.generate_password_hash(new_pass.encode('utf-8')) #encrypting passsword and scrambling password into byte string or ascii instead of utf-8
        self._password_hash = pass_hash.decode('utf-8') #storing to a string instead of a byte string

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8')) # check if a password matches something in our db


    @validates('permission_level')
    def validate_permission_level(self, key, value):
        # Define the acceptable permission levels
        acceptable_levels = [1, 2, 3]

        if value in acceptable_levels:
            return value
        else:
            raise ValueError("Invalid permission level. Choose from 1, 2, or 3.")




class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    serialize_rules = ('-user.posts',)

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)  # Assuming you want to store video URLs or file paths
    description = db.Column(db.String)
    likes = db.Column(db.Integer, default=0)  # Number of likes for the post
    comments = db.Column(db.String)  # Assuming you want to store comments or content as text
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates= 'posts')





# class Dashboard(db.Model, SerializerMixin):
#     __tablename__ = 'dashboards'

#     id = db.Column(db.Integer, primary_key = True)


#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


#     user = db.relationship('User', back_populates= 'dashboard')

