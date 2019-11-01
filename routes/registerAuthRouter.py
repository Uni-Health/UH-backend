def handler(request, hashlib, connection, pymysql, jsonify):
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
            })
        return jsonify({
            'status': 200,
            'msg': 'Success',
            'username': username,
        })
    except:
        return jsonify({
            'status': 400,
            'msg': 'An unknown error has occured. Please try again.'
        })