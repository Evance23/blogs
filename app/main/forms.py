from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required,Email
from ..models import User
from flask_login import current_user
from flask_wtf.file import FileField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')
    username = StringField('Input your username',validators=[Required()])
    email = StringField('Email', validators=[Required(),Email()])
    profile_pic = FileField('profile pic', validators=[Required()]) 


class CreateBlog(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Blog Content', validators=[Required()])
    submit = SubmitField('Post')
    

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("This Email has been taken")
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("This username has been taken")


 