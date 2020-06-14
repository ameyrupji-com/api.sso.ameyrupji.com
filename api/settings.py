from api import app
from flask_sqlalchemy import SQLAlchemy
from .dialects import S3SQLiteDialect

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/' # TODO: this will have to change

# Flask-SQLAlchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = 's3sqlite:///api.sso.beta.ameyrupji.com-data.sqlite'  # File-based SQL database


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids SQLAlchemy warning

# Flask-User settings
# app.config['USER_APP_NAME'] = "SSO AmeyRupji.com App"  # Shown in and email templates and page footers
# app.config['USER_ENABLE_EMAIL'] = False  # Disable email authentication
# app.config['USER_ENABLE_USERNAME'] = True  # Enable username authentication
# app.config['USER_REQUIRE_RETYPE_PASSWORD'] = False  # Simplify register form


# Much better to set this via some other mechanism, but this keeps all
# the settings in this one file
# import os
# os.environ['S3SQLite_bucket'] = 'api.sso.beta.ameyrupji.com-data'
print("Setting s3sqlite dialect!")
from sqlalchemy.dialects import registry
registry.register(name="s3sqlite", modulepath="api.dialects", objname="S3SQLiteDialect")


print("Loaded SQLAlchemy Dialects")


db = SQLAlchemy(app)

