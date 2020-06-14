from flask import Flask

# static files are disabled as this is more of an api
print("Starting app!")
app = Flask(__name__, static_folder=None)

from api import settings, models, views, dummy_data

