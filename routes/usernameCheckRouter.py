def handler(request, connection, jsonify):
    try:
        requestData = request.get_json()
        username = requestData['username']
        with connection.cursor() as cursor:
            query = "SELECT * FROM person WHERE username = %s"
            cursor.execute(query, username)
        data = cursor.fetchone()
        if data:
            return jsonify({
                'status': 403,
                'msg': 'This username has been taken.'
            })
        return jsonify({
            'status': 200,
            'msg': 'Success'
        })
    except:
        return jsonify({
            'status': 400,
            'msg': 'An unknown error has occured. Please try again.'
        })