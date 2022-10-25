from app import api
from flask_restx import Resource
from app.schemas.commentary_schema import CommentaryRequestSchema
from app.controllers.commentary_controller import CommentaryController
from flask_jwt_extended import jwt_required

namespace = api.namespace(
    name='Commentary',
    description='Commentaries Routes',
    path='/commentaries'
)

request_schema = CommentaryRequestSchema(namespace)



@namespace.route('/')
@namespace.doc(security='Bearer')
class Commentary(Resource):
    # @jwt_required()
    # @namespace.expect(request_schema.all())
    # def get(self):
    #     '''Publication list'''
    #     query_params =  request_schema.all().parse_args()
    #     controller = CommentaryController()
    #     return controller.all( query_params['per_page'], query_params['page'])

    @jwt_required()
    @api.expect(request_schema.create(), validate=True)
    def post(self):
        '''Commentary Created'''
        form = request_schema.create().parse_args()
        print(form)
        controller = CommentaryController()
        return controller.create(form)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class CommentarybydID(Resource):
    @jwt_required()
    def get(self, id):
        '''Commentary By ID'''
        controller = CommentaryController()
        return controller.getById(id)

    @jwt_required()
    @api.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Commentary Update'''
        form = request_schema.update().parse_args()
        controller = CommentaryController()
        return controller.update(id, form)

    @jwt_required()
    def delete(self, id):
        '''Commentary delete'''
        controller = CommentaryController()
        return controller.delete(id)


api.add_namespace(namespace)