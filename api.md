# API documentation for Uni-Health backend

## Error messages

| Error type | Code |
| --- | --- |
| ALREADY_EXIST | `{'status': 400, 'msg': 'An user has existed.' }` |
| DOES_NOT_EXIST | `{'status': 409, 'msg': 'Does not exists.'}` |
| EMPTY | `{'status': 202, 'msg': 'None'}` |
| HEADER_NOT_FOUND | `{'status': 999, 'msg': 'Header does not exists.'}` |
| INVALID_INPUT | `{'status': 422, 'msg': 'Invalid input.'}` |
| NO_INPUT_400 | `{'status': 400, 'msg': 'No input data provided.'}` |
| NOT_ADMIN | `{'status': 999, 'msg': 'Admin permission denied.'}` |
| NOT_FOUND_404 | `{'status': 404, 'msg': 'Resource could not be found.'}` |
| SERVER_ERROR_500 | `{'status': 500, 'msg': 'An error occured.'}` |
| UNAUTHORIZED | `{'status': 401, 'msg': 'Unauthorized'}` |
| UNKNOWN_ERROR | `{'status': 400, 'msg': 'An unknown error has occured. Please try again.' }` |

## Register API
**POST**  **/register**

### Request Value
```
{
    "username": "test",
    "phone": "12345678",
    "password": "test",
    "role": "doctor" // Determine whether he/she is a doctor or patient
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'username': "test",
}
```
or Error Messages

## Login API
**POST** **/login**

### Request Value
```
{
    "phone": "12345678",
    "password": "test",
    "role": "doctor" // Determine whether he/she is a doctor or patient
}
```
Or Error Messages

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'role': 'patient',
    'session': '12345678',
}
```