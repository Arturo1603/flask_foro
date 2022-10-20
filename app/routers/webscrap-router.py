from app import api
from flask import request
from flask_restx import Resource
from app.schemas.webscrap_schema import WebScrapRequestSchema
from app.controllers.webscrap_controller import WebScrapController

namespace = api.namespace(
    name='Scraps',
    description='Scraps Route',
    path='/scrap'
)

request_schema = WebScrapRequestSchema(namespace)


@namespace.route('/')
class WebScrap(Resource):

    @namespace.expect(request_schema.scrap())
    def get(self):
        '''Scrap list '''
        query_params = request_schema.scrap().parse_args()
        controller = WebScrapController()
        return controller.scrap(query_params['searcher'])


api.add_namespace(namespace)
