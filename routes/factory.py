from flask_restful import Resource

class RegisterFactory(Resource):
    def __init__(self, registerRouter):
        self.route = registerRouter
    
    def get(self):
        return self.route.get()
    
    def post(self):
        return self.route.post()
    
    def put(self):
        return self.route.put()

    def delete(self):
        return self.route.delete()