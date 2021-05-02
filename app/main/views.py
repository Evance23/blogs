import os
from flask import render_template,redirect,url_for,abort,request,flash
from app.main import main
from .forms import UpdateProfile,NewBlog
from flask_login import login_required,current_user
from ..email import mail_message


