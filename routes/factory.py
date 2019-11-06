
from flask import request
from .usernameCheckRouter import *
from .registerAuthRouter import *
from .logoutRouter import *
from .loginAuthRouter import *
from .authorizeRouter import *
import hashlib


class RegisterFactory:
    def register(self, role):
        register = get_register(role)
        return register


def get_register(role):
    if role == 'patient':
        return RegisterAuthRouter
