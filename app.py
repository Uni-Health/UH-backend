from flask import Flask, request, session, send_file, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
import hashlib
import pymysql.cursors
from functools import wraps

STATIC_DIR = os.path.join(os.getcwd(), 'dist')
app = Flask(__name__, static_url_path='/dist')
app.secret_key = "super secret key"
IMAGES_DIR = os.path.join(os.getcwd(), "images")
CORS(app, supports_credentials=True)

db_password = '' if len(sys.argv) == 1 else 'root'
connection = pymysql.connect(host="localhost",
                             user="root",
                             password=db_password,
                             db="unihealth",
                             charset="utf8mb4",
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)

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

@app.route('/authorize', methods=['GET'])
def auth():
    return authorizeRouter.handler(session, connection, jsonify)

@app.route("/loginAuth", methods=["POST"])
def loginAuth():
    return loginAuthRouter.handler(request, connection, hashlib, session, jsonify)

@app.route("/usernameCheck", methods=["POST"])
def usernameCheck():
    return usernameCheckRouter.handler(request, connection, jsonify)

@app.route("/registerAuth", methods=["POST"])
def registerAuth():
    return registerAuthRouter.handler(request, hashlib, connection, pymysql, jsonify)

@app.route("/logout", methods=["GET"])
def logout():
    return logoutRouter.handler(session, jsonify)

if __name__ == "__main__":
    if not os.path.isdir("images"):
        os.mkdir(IMAGES_DIR)
    app.debug = True
    app.run(host="0.0.0.0")