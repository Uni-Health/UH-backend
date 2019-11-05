class RegisterAuthRouter():
    def __init__(self, request, hashlib, db):
        self.request = request
        self.hashlib = hashlib
        self.db = db
    
    def get(self):
        return '', 202
    
    def post(self):
        try:
            requestData = request.get_json()
            username = requestData["username"]
            plaintextPasword = requestData["password"]
            hashedPassword = hashlib.sha256(plaintextPasword.encode("utf-8")).hexdigest()
            firstName = requestData["firstName"]
            lastName = requestData["lastName"]

            try:
                with connection.cursor() as cursor:
                    query = "INSERT INTO person (username, password, fname, lname) VALUES (%s, %s, %s, %s)"
                    cursor.execute(query, (username, hashedPassword, firstName, lastName))
                    connection.commit()
            except pymysql.err.IntegrityError:
                return jsonify({
                    'status': 400,
                    'msg': 'An user has existed.'
                }), 400
            return jsonify({
                'status': 200,
                'msg': 'Success',
                'username': username,
            }), 200
        except:
            return jsonify({
                'status': 400,
                'msg': 'An unknown error has occured. Please try again.'
            }), 400
    
    def put(self):
        return '', 202

    def delete(self):
        return '', 202