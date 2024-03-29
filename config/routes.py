from flask_restful import Api
from resources import *
from error.errors import *

def init_routes(app):
    api = Api(app)

    api.add_resource(RegisterAuth, "/register")
    api.add_resource(LoginAuth, '/login')
    api.add_resource()


# required login
def login_required(f):
    @wraps(f)
    def dec(*args, **kwargs):
        if not "phone number" in session:
            return UNAUTHORIZED
        return f(*args, **kwargs)
    return dec