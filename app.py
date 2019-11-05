import os
import sys
import hashlib
from functools import wraps
from flask import Flask, request, session, send_file, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, abort, Api, Resource
from routes import *
from models import *

# project configs
STATIC_DIR = os.path.join(os.getcwd(), 'dist')
app = Flask(__name__, static_url_path='/dist')
app.config.from_pyfile(os.path.abspath('app.cfg'))
IMAGES_DIR = os.path.join(os.getcwd(), "images")
CORS(app, supports_credentials=True)
db = SQLAlchemy(app)
api = Api(app)

# required login
def login_required(f):
    @wraps(f)
    def dec(*args, **kwargs):
        if not "username" in session:
            return jsonify({
                'status': 401,
                'msg': 'Unauthorized'
            })
        return f(*args, **kwargs)
    return dec

# router for authorize
@app.route('/authorize', methods=['GET'])
def auth():
    return authorizeRouter.handler(session, db, jsonify)

# router for login authentication
@app.route("/loginAuth", methods=["POST"])
def loginAuth():
    return loginAuthRouter.handler(request, db, hashlib, session, jsonify)

# router for checking username usage
@app.route("/usernameCheck", methods=["POST"])
def usernameCheck():
    return usernameCheckRouter.handler(request, db, jsonify)

# router for registration authentication
api.add_resource(RegisterFactory, "/registerAuth", resource_class_kwargs={'route': RegisterAuthRouter(request, hashlib, db)})

# router for logging out of the system
@app.route("/logout", methods=["GET"])
def logout():
    return logoutRouter.handler(session, jsonify)

if __name__ == "__main__":
    if not os.path.isdir("images"):
        os.mkdir(IMAGES_DIR)
    app.debug = True
    app.run(host="0.0.0.0")