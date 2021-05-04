from flask import render_template, request
from . import main
from .. import db
from ..models import Followers
from ..email import welcome_message

@main.app_errorhandler(404)
def notfound(error):
    """
    Function to render the 404 error page
    """
    if request.method == "POST":
        new_sub = Followers(email = request.form.get("follower"))
        db.session.add(new_sub)
        db.session.commit()
        welcome_message("Thank you for subscribing to the My-blog", 
                        "email/welcome")
    return render_template("notfound.html"),404