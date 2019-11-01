def handler(request, connection, hashlib, session, jsonify):
    try:
        # Parse JSON data in request body
        requestData = request.get_json() # A Python Dictionary
        username = requestData["username"]
        plaintextPasword = requestData["password"]
        hashedPassword = hashlib.sha256(plaintextPasword.encode("utf-8")).hexdigest()

        with connection.cursor() as cursor:
            query = "SELECT * FROM person WHERE username = %s AND password = %s"
            cursor.execute(query, (username, hashedPassword))
        data = cursor.fetchone()
        if data:
            session["username"] = username
            # Use jsonify to send a JSON response
            return jsonify({
                'status': 200,
                'msg': 'Success',
                'username': username,
            })
        return jsonify({
            'status': 403,
            'msg': 'Incorrect username or password'
        })
    except:
        return jsonify({
            'status': 400,
            'msg': 'An unknown error has occurred. Please try again.'
        })