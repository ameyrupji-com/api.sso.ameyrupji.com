import os

from api import app
from api.settings import db
from flask import Flask, request
from .models import Role, User, UserRoles
from flask_restless import APIManager

@app.route('/about')
def about():
  return {
    "app": "SSO - Amey Rupji",
    "version": "1.0 - Beta",
    "db": os.environ['S3SQLite_bucket']
  }

@app.route("/")
def index():
    routes = [{"url": rule.rule, "methods": list(rule.methods)} for rule in app.url_map.iter_rules()]
    return {"base_url": request.base_url, "routes": routes }



# @app.route("/roles")
# def roles():
#     roles = Role.query
#     return {"count": roles.count(), "results": [r.as_dict() for r in roles]}

# @app.route("/roles/add", methods=['POST'])
# def roles():
#     roles = Role.query
#     return {"count": roles.count(), "results": [r.as_dict() for r in roles]}

# Create the Flask-Restless API manager.
url_prefix= "/"
manager = APIManager(app, flask_sqlalchemy_db=db)


# Create API endpoints, which will be available at /<tablename> by
# default. Allowed HTTP methods can be specified as well.
# manager.create_api(Person, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Role, methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'], url_prefix=url_prefix)
manager.create_api(User, methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'], url_prefix=url_prefix, exclude_columns=['password'])
manager.create_api(UserRoles, methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'], url_prefix=url_prefix)

## querry filter for number of results in ?results_per_page=


## TODO: Model validations
# https://flask-restless.readthedocs.io/en/stable/customizing.html#capturing-validation-errors


## TODO: enable CORS
# https://flask-restless.readthedocs.io/en/stable/customizing.html#enabling-cross-origin-resource-sharing-cors