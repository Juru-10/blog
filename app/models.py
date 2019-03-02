from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class Writer(UserMixin,db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     # bio = db.Column(db.String)
#     profile_pic_path = db.Column(db.String())
#     pass_secure = db.Column(db.String(255))
#     posts = db.relationship('Post', backref ='writer',lazy = "dynamic")
#     # comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
#     # votes = db.relationship('Vote',backref = 'user',lazy = "dynamic")
#
#     @property
#     def password(self):
#         raise AttributeError('You cannot read the password attribute')
#
#     @password.setter
#     def password(self, password):
#         self.pass_secure = generate_password_hash(password)
#
#
#     def verify_password(self,password):
#         return check_password_hash(self.pass_secure,password)
#
#     def __repr__(self):
#         return f'User {self.username}'
#

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    # subcribers = db.relationship('Subscriber', backref ='user',lazy = "dynamic")
    posts = db.relationship('Post', backref ='user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Subscriber(db.Model):
    __tablename__ = 'subscribers'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
            return f'User {self.username}'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    comments = db.relationship('Comment',backref ='comments',lazy = "dynamic")

    @classmethod
    def get_pitches(cls,id):
        posts = Post.query.filter_by(user_id=id).all()
        return posts


    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    def __repr__(self):
        return f'User {self.name}'

class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer,primary_key = True)
    author=db.column(db.String)
    quote=db.column(db.String)
    permalink=db.column(db.String)

    @classmethod
    def get_comments(cls,id):
        quotes = Quote.query.filter_by(id=quotes.id).all()
        return quotes

    def __repr__(self):
        return f'Quote {self.quote}'
