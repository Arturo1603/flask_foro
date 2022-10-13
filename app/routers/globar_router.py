from  app import api
from flask_restx import Resource

global_ns= api.namespace(
    name='Global',
    description='Rutas Globales',
    path='/global'
)

@global_ns.route('/')
class Global(Resource):
    def get(self):
        return {
            "message": "Hola mundo"
        }
    
    def post(self):
        return{
            "message": "esto es post"
        }

@global_ns.route('/<int:id>')
class GlobalById(Resource):
    def put(self, id):
        return {
            "message": f'updated id: {id}'
        }

    def delete(self, id):
        return {
            "message": f'deleted id: {id} '
        }

api.add_namespace(global_ns)

