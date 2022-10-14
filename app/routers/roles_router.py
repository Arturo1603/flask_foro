from app import api
from flask import request
from flask_restx import Resource
from app.schemas.roles_schema import RolesRequestSchema
from app.controllers.roles_controller import RolesController

namespace = api.namespace(
    name='Roles',
    description='Roles Routes',
    path='/roles'
)

request_schema = RolesRequestSchema(namespace)


@namespace.route('/')
class Roles(Resource):

    def get(self):
        '''Roles List'''
        controller = RolesController()
        return controller.all()

    @api.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Roles Creation'''
        controller = RolesController()
        # con la clase request de flask capturamos el bodyrequest
        return controller.create(request.json)


@namespace.route('/<int:id>')
class RolesByID(Resource):

    def get(self, id):
        '''Get a rol by ID'''
        controller = RolesController()
        return controller.getById(id)

    @api.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Role Update'''
        controller = RolesController()
        return controller.update(id, request.json)


    def delete(self, id):
        '''Rol Delete'''
        controller = RolesController()
        return controller.delete(id)

api.add_namespace(namespace)
