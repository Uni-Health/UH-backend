from error.errors import *
from resources import *
from handlers import *

def registerHandlerFactory(role):
    if role == 'patient':
        return registerPatientHandler
    elif role == 'doctor':
        return registerDoctorHandler
    else:
        return registerError

def registerError():
    return INVALID_INPUT