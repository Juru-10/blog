from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Writer(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    # comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    # vote_id = db.Column(db.Integer,db.ForeignKey('votes.id'))
    bio = db.Column(db.String)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref ='user',lazy = "dynamic")
    # comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    # votes = db.relationship('Vote',backref = 'user',lazy = "dynamic")

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


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    # comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    # vote_id = db.Column(db.Integer,db.ForeignKey('votes.id'))
    bio = db.Column(db.String)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref ='user',lazy = "dynamic")
    # comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    # votes = db.relationship('Vote',backref = 'user',lazy = "dynamic")

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

class Post(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    # comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    # vote_id = db.Column(db.Integer,db.ForeignKey('votes.id'))
    comments = db.relationship('Comment',backref ='comments',lazy = "dynamic")
    votes = db.relationship('Vote',backref ='vote',lazy = "dynamic")

    # users = db.relationship('User',backref = 'pitch',lazy="dynamic")

    # def save_pitch(self):
    #     db.session.add(self)
    #     db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(user_id=id).all()
        return pitches


    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    # user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    # users = db.relationship('User',backref = 'comment',lazy="dynamic")

    # def save_comment(self):
    #     db.session.add(self)
    #     db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    def __repr__(self):
        return f'User {self.name}'
