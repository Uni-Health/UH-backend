def handler(session, jsonify):
    try:
        session.pop("username")
    except:
        return jsonify({
            'status': 400,
            'msg': 'Unknown server error!'
        })
    return jsonify({
        'status': 200,
        'msg': 'Logged out',
    })