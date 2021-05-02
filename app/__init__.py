from flask import Flask
from config import Config
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads,IMAGES

db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

#CONFIGURE UploadSet
configure_uploads(app,photos)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #flask extensions
    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    return app