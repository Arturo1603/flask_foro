from app import api
from flask import request
from flask_restx import Resource
from app.schemas.roles_schema import RolesRequestSchema
from app.controllers.roles_controller import RolesController
from flask_jwt_extended import jwt_required, current_user

namespace = api.namespace(
    name='Roles',
    description='Roles Routes',
    path='/roles'
)

request_schema = RolesRequestSchema(namespace)


@namespace.route('/')
# @namespace.doc(security='Bearer')
class Roles(Resource):
    # @jwt_required()
    def get(self):
        '''Roles List'''
        print(current_user)
        controller = RolesController()
        return controller.all()

    # @jwt_required()
    @api.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Roles Creation'''
        controller = RolesController()
        # con la clase request de flask capturamos el bodyrequest
        return controller.create(request.json)

# @namespace.doc(security='Bearer')
@namespace.route('/<int:id>')
class RolesByID(Resource):

    # @jwt_required()
    def get(self, id):
        '''Get a rol by ID'''
        controller = RolesController()
        return controller.getById(id)

    # @jwt_required()
    @api.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Role Update'''
        controller = RolesController()
        return controller.update(id, request.json)


    # @jwt_required()
    def delete(self, id):
        '''Rol Delete'''
        controller = RolesController()
        return controller.delete(id)

api.add_namespace(namespace)
