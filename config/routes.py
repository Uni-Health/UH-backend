from flask_restful import Api
from resources import *


def init_routes(app):
    api = Api(app)

    api.add_resource(RegisterPatientAuth, "/abc")
