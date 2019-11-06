import hashlib
import logging
from flask_restful import Resource
from flask import request
from database.database import db
from error.errors import *
from models.doctor import *

class RegisterPatientAuth(Resource):
    def get(self):
        return EMPTY

    def post(self):
        print(request.get_json())
        try:
            requestData = request.get_json()
            username = requestData["username"]
            phone = requestData["phone"]
            plaintextPasword = requestData["password"]
            hashedPassword = hashlib.sha256(
                plaintextPasword.encode("utf-8")).hexdigest()
        
        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT

        if username is None or hashedPassword is None or phone is None:
            return INVALID_INPUT

        doctor = Doctor.query.filter_by(phone=phone).first()

        if patient is not None:
            return ALREADY_EXIST

        doctor = Doctor(username, str(phone), str(hashedPassword))
        db.session.add(patient)
        db.session.commit()
        print(doctor)

        return {
            'status': 200,
            'msg': 'Success',
            'username': username,
        }, 200

    def put(self):
        return EMPTY

    def delete(self):
        return EMPTY
