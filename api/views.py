from api import app
from flask import Flask, request

@app.route('/about')
def about():
  return {
    "app": "SSO - Amey Rupji",
    "version": "1.0 - Beta",
  }

@app.route("/")
def index():
    routes = [{"url": rule.rule, "methods": list(rule.methods)} for rule in app.url_map.iter_rules()]
    return {"base_url": request.base_url, "routes": routes }


