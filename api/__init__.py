from flask import Flask


# Much better to set this via some other mechanism, but this keeps all
# the settings in this one file
import os
print("Setting S3SQLite_bucket to 'api.sso.beta.ameyrupji.com-data'")
os.environ['S3SQLite_bucket'] = 'api.sso.beta.ameyrupji.com-data'


# this is the important change, it imports sqlalchemy-s3sqlite at runtime
# print("Setting s3sqlite dialect!")
# from sqlalchemy.dialects import registry
# registry.register("s3sqlite", ".dialect", "S3SQLiteDialect")

# static files are disabled as this is more of an api
print("Starting app!")
app = Flask(__name__, static_folder=None)

from api import settings, models, views

