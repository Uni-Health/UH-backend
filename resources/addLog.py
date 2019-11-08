import logging
from flask import request
from resources import *
from handlers.addLogHandlerFactory import *
from flask_restful import Resource

class AddLog(Resource):
    def get(self):
        return EMPTY

    def post(self):
        requestData = request.get_json()
        t = requestData["type"]
        loginHandler = loginHandlerFactory(t)
        
        return loginHandler()

    def put(self):
        return EMPTY

    def delete(self):
        return EMPTY
