def handler(session, connection, jsonify):
    if 'username' in session:
        username = session['username']
        try:
            with connection.cursor() as cursor:
                query = 'SELECT avatar FROM Person WHERE username = %s'
                cursor.execute(query, username)
            data = cursor.fetchone()
        except:
            return jsonify({
                'status': 400,
                'msg': 'Database error',
            })
        if data:
            return jsonify({
                'status': 200,
                'msg': 'You are authorized',
                'username': username,
                'avatar': data['avatar']
            })
        return jsonify({
            'status': 404,
            'msg': 'No user is found',
        })
    return jsonify({
        'status': 401,
        'msg': 'Unauthorized'
    })