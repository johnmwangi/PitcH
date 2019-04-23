import os

class Config:

    SECRET_KEY="john"
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://john:1234@localhost/pitches'


    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch'

    SENDER_EMAIL = ''



class ProdConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://john:1234@localhost/pitches'


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
