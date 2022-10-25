from app import api
from flask import request
from flask_restx import Resource
from app.schemas.publication_schema import PublicationRequestSchema
from app.controllers.publication_controller import PublicationController
from flask_jwt_extended import jwt_required, current_user

namespace = api.namespace(
    name='Publication',
    description='Publications Routes',
    path='/publications'
)

request_schema = PublicationRequestSchema(namespace)


@namespace.route('/')
@namespace.doc(security='Bearer')
class Users(Resource):
    @jwt_required()
    @namespace.expect(request_schema.all())
    def get(self):
        '''Publication list'''
        query_params =  request_schema.all().parse_args()
        controller = PublicationController()
        return controller.all( query_params['per_page'], query_params['page'])

    @jwt_required()
    @api.expect(request_schema.create(), validate=True)
    def post(self):
        '''Publication Created'''
        form = request_schema.create().parse_args()
        print(form)
        controller = PublicationController()
        return controller.create(form)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class UsersbydID(Resource):
    @jwt_required()
    def get(self, id):
        '''Publication By ID'''
        controller = PublicationController()
        return controller.getById(id)

    @jwt_required()
    @api.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Publication Update'''
        form = request_schema.update().parse_args()
        controller = PublicationController()
        return controller.update(id, form)

    @jwt_required()
    def delete(self, id):
        '''Publication delete'''
        controller = PublicationController()
        return controller.delete(id)


api.add_namespace(namespace)