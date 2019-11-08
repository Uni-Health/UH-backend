from error.errors import *
from resources import *
from handlers import *

def loginHandlerFactory(role):
    if role == 'patient':
        return loginPatientHandler
    elif role == 'doctor':
        return loginDoctorHandler
    else:
        return loginError

def loginError():
    return INVALID_INPUT