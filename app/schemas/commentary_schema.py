from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.commentary_model import CommentaryModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage


class CommentaryRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('per_page', type=int, default=1, location='args')
        parser.add_argument('page', type=int, default=1, location='args')
        
        return parser
    def create(self):

        parser = RequestParser()
        parser.add_argument('message', type=str, required=True,  location='form')
        parser.add_argument('image_url', type=FileStorage,
                            required=True,  location='files')
        parser.add_argument('publication_id', type=int, required=True, location='form')
        return parser


    def update(self):
        parser = RequestParser()
        parser.add_argument('description', type=str, required=False,  location='form')
        parser.add_argument('image_url', type=FileStorage,
                            required=False,  location='files') 

        return parser


class CommentaryResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CommentaryModel
        ordered = True

    users = Nested('UserResponseSchema', exclude=['commentary'], many=False)
    reply_comment_commentary = Nested('ReplyCommentResponseSchema', exclude=['commentary_reply_comment'], many=True)