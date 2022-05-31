import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./app.db'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    print(SQLALCHEMY_DATABASE_URI)
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
