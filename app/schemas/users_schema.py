from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.users_model import UserModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

class UserRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('per_page', type=int, default=1, location='args')
        parser.add_argument('page', type=int, default=1, location='args')
        return parser

    def create(self):


        parser = RequestParser()
        parser.add_argument('name', type=str, required=True,  location='form')
        parser.add_argument('last_name', type=str,
                            required=True,  location='form')
        parser.add_argument('image_url', type=FileStorage,
                            required=False,  location='files')
        parser.add_argument('email', type=str, required=True,  location='form')

        parser.add_argument('username', type=str,
                            required=True,  location='form')
        parser.add_argument('password', type=str,
                            required=True,  location='form')

        return parser


    def update(self):
        parser = RequestParser()
        parser.add_argument('name', type=str, required=False,  location='form')
        parser.add_argument('last_name', type=str,
                            required=False,  location='form')
        parser.add_argument('image_url', type=FileStorage,
                            required=False,  location='files')


        parser.add_argument('username', type=str,
                            required=False,  location='form')

        return parser


class UserResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        ordered = True
        exclude = ['password']

    role = Nested('RolesResponseSchema', exclude=['users'], many=False)
    publication = Nested('PublicationResponseSchema', exclude=['users'],  many=True)
    reply_comment = Nested('ReplyCommentResponseSchema', exclude=['users'], many=True)