from . import db,login_manager
from flask_login import current_user,UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User (UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(20), nullable=False, default='default.jpg')
    hashed_password = db.Column(db.String(250)) 
    bio = db.Column(db.String(255),default = 'My default Bio') 
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hashed_password,password) 
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment', backref='blog', lazy='dynamic')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Blog{self.title}"

    @classmethod
    def get_blog(id):
        blog = Blog.query.filter_by(id = id).first()
        return blog
        
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    comment = db.Column(db.Text(),nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def get_comment(id):
        comment = Comment.query.all(id=id)
        return comment

    def __repr__(self):
        return f'comment{self.comment}'


class Follower(db.Model):
    __tablename__ = 'followers'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True, index=True)
    

    def save_follower(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'Follower {self.email}'
        
class Quote:
    __tablename__='quotes'
    '''
    Blueprint class for quotes consumed from API
    '''
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote