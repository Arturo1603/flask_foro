
from flask_restx.reqparse import RequestParser

class WebScrapRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def scrap(self):
        parser=RequestParser()
        parser.add_argument('searcher', type=str, location='args')
        return parser