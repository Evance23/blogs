import os 

class Config:
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLAlchemy_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLAlchemy_TRACK_MODIFICATIONS=True

    UPLOADED_PHOTOS_DEST='app/static/photos'
    DEBUG = True