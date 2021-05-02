from wtforms.validators import Required, Email, EqualTo, Length
from ..models import User
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from flask_wtf import FlaskForm
from wtforms import ValidationError



class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    username = StringField('Enter your Username',validators=[Required()])
    email = StringField('Your Email Address', validators=[Required(), Email()]) 
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Password must match')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')

#Custom email validation
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError("This email has been taken")
#Custom username validation
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValiadtionError("This username has already been taken")
