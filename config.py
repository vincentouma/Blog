import os

class Config:
    #keys required by flask extensions
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #database
    SQLALCHEMY_DATABASE_URI = ''


    #set email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAI_PASSWORD= os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG=True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}