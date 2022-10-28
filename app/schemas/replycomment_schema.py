from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.replycomment_model import ReplyCommentModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage


class ReplyCommentRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('per_page', type=int, default=1, location='args')
        parser.add_argument('page', type=int, default=1, location='args')

        return parser

    def create(self):

        parser = RequestParser()
        parser.add_argument('message', type=str,
                            required=True,  location='form')
        parser.add_argument('image_url', type=FileStorage,
                            required=False,  location='files')
        parser.add_argument('commentary_id', type=int,
                            required=True, location='form')
        return parser

    def update(self):
        parser = RequestParser()
        parser.add_argument('description', type=str,
                            required=False,  location='form')
        parser.add_argument('image_url', type=FileStorage,
                            required=False,  location='files')

        return parser


class ReplyCommentResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ReplyCommentModel
        ordered = True

    users = Nested('UserResponseSchema', exclude=['reply_comment'], many=False)
    commentary_reply_comment = Nested('CommentaryResponseSchema', exclude=[
                                      'reply_comment_commentary'], many=False)
    publication_reply = Nested('PublicationResponseSchema', exclude=[
                                      'reply_publication'], many=False)
