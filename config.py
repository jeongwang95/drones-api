import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# give access to the project in ANY operating system we find ourselves in
# allows outside files/folders to be added to the project from the base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set Config variables for the flask app.
    Using Environent Variables where available otherwise
    create the config variable if not done already
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Key not found'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # turn off update messages from sqlalchemy