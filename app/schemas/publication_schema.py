from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.publication_model import PublicationModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

class PublicationRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('per_page', type=int, default=1, location='args')
        parser.add_argument('page', type=int, default=1, location='args')
        
        return parser
    def create(self):

        parser = RequestParser()
        parser.add_argument('description', type=str, required=True,  location='form')
        parser.add_argument('title', type=str, required=True,  location='form')
        parser.add_argument('image_url', type=FileStorage,
                            required=True,  location='files')
        return parser


    def update(self):
        parser = RequestParser()
        parser.add_argument('description', type=str, required=False,  location='form')
        parser.add_argument('title', type=str, required=False,  location='form')
        parser.add_argument('image_url', type=FileStorage,
                            required=False,  location='files') 

        return parser


class PublicationResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PublicationModel
        ordered = True

    users = Nested('UserResponseSchema', exclude=['publication'], many=False)