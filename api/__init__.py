from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# static files are disabled as this is more of an api
app = Flask(__name__, static_folder=None)
db = SQLAlchemy(app)

from api import settings, models, views

