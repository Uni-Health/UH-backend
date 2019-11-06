import os
import json
from database.database import db
from models.base import *


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column('id', db.Integer, primary_key=True,
                   unique=True, nullable=False)
    name = db.Column('name', db.String, nullable=False)
    email = db.Column('email', db.String, nullable=False)
    illness = db.Column('illness', JsonEncodedDict)

    def __init__(self, name, email, illness):
        self.name = name
        self.email = email
        self.illness = illness

    def __repr__(self):
        return '<Person {}>'.format(self.name)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
