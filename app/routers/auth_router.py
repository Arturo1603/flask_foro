from app import api
from flask_restx import Resource
from app.controllers.auth_controller import AuthController
from flask import request
from app.schemas.auth_schema import AuthRequestSchema
from flask_jwt_extended import jwt_required


namespace = api.namespace(
    name='Authentication',
    description='Auth Routes',
    path='/auth'
)

request_schema = AuthRequestSchema(namespace)

@namespace.route('/signin')
class SignIn(Resource):
    
    @api.expect(request_schema.signIn(), validate=True)
    def post(self):
        '''Token Create'''
        controller = AuthController()
        print(request.json)
        return controller.signIn(request.json)

# reset passsword
@namespace.route('/reset_password')
class ResetPassword(Resource):
    @namespace.expect(request_schema.resetPassword(), validate=True)
    def post(self):
        ''' Restear la contrasenia de un usuario '''
        controller = AuthController()
        return controller.resetPassword(request.json)

@namespace.route('/token/refresh')
class TokenRefresh(Resource):

    @namespace.expect(request_schema.refreshToken())
    @jwt_required(refresh=True)
    def post(self):
        '''Get a new AccessToken for RefreshToken'''
        pass


api.add_namespace(namespace)