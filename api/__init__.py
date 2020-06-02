from flask import Flask

app = Flask(__name__)

from api import settings, models, views  # NOQA