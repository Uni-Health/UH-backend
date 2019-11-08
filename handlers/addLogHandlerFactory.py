from error.errors import *
from resources import *
from handlers import *

def addLogHandlerFactory(t):
    if t == 'simple':
        return addLogHander
    elif t == 'detailed':
        return addDetailLogHandler
    else:
        return addLogError

def addLogError():
    return INVALID_INPUT