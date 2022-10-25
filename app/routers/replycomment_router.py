from app import api
from flask_restx import Resource
from app.schemas.replycomment_schema import ReplyCommentRequestSchema
from app.controllers.replycomment_controller import ReplyCommentController
from flask_jwt_extended import jwt_required

namespace = api.namespace(
    name='ReplyCommentary',
    description='Reply Commentary Routes',
    path='/replycomment'
)

request_schema = ReplyCommentRequestSchema(namespace)



@namespace.route('/')
@namespace.doc(security='Bearer')
class ReplyCommentary(Resource):
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
        '''Reply Commentary Created'''
        form = request_schema.create().parse_args()
        print(form)
        controller = ReplyCommentController()
        return controller.create(form)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class ReplyCommentarybydID(Resource):
    @jwt_required()
    def get(self, id):
        '''Reply Commentary By ID'''
        controller = ReplyCommentController()
        return controller.getById(id)

    @jwt_required()
    @api.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Reply Commentary Update'''
        form = request_schema.update().parse_args()
        controller = ReplyCommentController()
        return controller.update(id, form)

    @jwt_required()
    def delete(self, id):
        '''Reply Commentary delete'''
        controller = ReplyCommentController()
        return controller.delete(id)


api.add_namespace(namespace)