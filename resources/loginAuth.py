import logging
from flask import request
from resources import *
from handlers.loginHandlerFactory import *
from flask_restful import Resource

class LoginAuth(Resource):
    def get(self):
        return EMPTY

    def post(self):
        requestData = request.get_json()
        role = requestData["role"]
        loginHandler = loginHandlerFactory(role)
        
        return loginHandler()

    def put(self):
        return EMPTY

    def delete(self):
        return EMPTY
