#!/usr/bin/python
# -*- coding: utf-8 -*-

SERVER_ERROR_500 = ({"msg": "An error occured."}, 500)
NOT_FOUND_404 = ({"msg": "Resource could not be found."}, 404)
NO_INPUT_400 = ({"msg": "No input data provided."}, 400)
INVALID_INPUT = ({'status': 422, "msg": "Invalid input."}, 422)
ALREADY_EXIST = ({'status': 400, 'msg': 'An user has existed.' }, 400)
UNKNOWN_ERROR = ({'status': 400, 'msg': 'An unknown error has occured. Please try again.' }, 400)
DOES_NOT_EXIST = ({"msg": "Does not exists."}, 409)
NOT_ADMIN = ({"msg": "Admin permission denied."}, 999)
HEADER_NOT_FOUND = ({"msg": "Header does not exists."}, 999)
EMPTY = ('', 202)