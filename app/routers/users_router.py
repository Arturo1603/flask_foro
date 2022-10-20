from app import api
from flask import request
from flask_restx import Resource
from app.schemas.users_schema import UserRequestSchema
from app.controllers.users_controller import UsersController

namespace = api.namespace(
    name='Users',
    description='Users Routes',
    path='/users'
)

request_schema = UserRequestSchema(namespace)


@namespace.route('/')
class Users(Resource):
    @namespace.expect(request_schema.all())
    def get(self):
        '''User list'''
        query_params =  request_schema.all().parse_args()
        controller = UsersController()
        return controller.all( query_params['per_page'], query_params['page'])

    @api.expect(request_schema.create(), validate=True)
    def post(self):
        '''User Created'''
        controller = UsersController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
class UsersbydID(Resource):
    def get(self, id):
        '''User By ID'''
        controller = UsersController()
        return controller.getById(id)

    @api.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''User Update'''
        controller = UsersController()
        return controller.update(id, request.json)

    def delete(self, id):
        '''User delete'''
        controller = UsersController()
        return controller.delete(id)


api.add_namespace(namespace)
