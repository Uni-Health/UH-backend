import json
from database.database import db
from models.base import *
from models.person import *

class Doctor(Person):
    __tablename__ = 'doctor'
    __mapper_args__ = {'polymorphic_identity': 'doctor'}

    def __init__(self, usrname, phone, password, role):
        self.usrname = usrname
        self.phone = phone
        self.password = password
        self.role = role

    def __repr__(self):
        return '<Doctor {}>'.format(self.usrname)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}