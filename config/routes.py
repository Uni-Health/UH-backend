from flask_restful import Api
from resources import *


def init_routes(app):
    api = Api(app)

    api.add_resource(RegisterAuth, "/register")
    # api.add_resource(RegisterPatientAuth, "/register")


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