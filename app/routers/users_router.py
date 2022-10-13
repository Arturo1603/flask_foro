from app import api
from flask_restx import Resource

namespace = api.namespace(
    name='Users',
    description='Users Routes',
    path='/users'
)


@namespace.route('/')
class Users(Resource):
    def get(self):
        return {
            "message": "Users list"
        }

    def post(self):
        return {
            "message": "User created"
        }


@namespace.route('/<int:id>')
class UsersbydID(Resource):
    def put(self, id):
        return {
            "message": f'updated id: {id}'
        }

    def delete(self, id):
        return {
            "message": f'deleted id: {id}'
        }


api.add_namespace(namespace)
