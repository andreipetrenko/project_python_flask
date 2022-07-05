from flask import request
from flask_restx import Resource

from ..unit.dto import ClientDto
from ..service.clients_service import create_new_client, get_all_clients, get_client_by_id


api = ClientDto.api
_client = ClientDto.client


@api.route('/all')
class GetClient(Resource):
    @api.doc('list of all client')
    @api.marshal_list_with(_client, envelope='data')
    def get(self):
        return get_all_clients()


@api.route('/<clnt_id>')
@api.param('clnt_id', 'The Client identifier')
@api.response(404, 'Client not found')
class GetClient(Resource):
    @api.doc('list of one client')
    @api.marshal_list_with(_client, envelope='data')
    def get(self, clnt_id):
        client_data = get_client_by_id(clnt_id)
        if not client_data:
            api.abort(404)
        else:
            return client_data


@api.route('/create')
class PostClient(Resource):
    @api.response(201, 'Client create success!')
    @api.doc('create a new client')
    @api.expect(_client, validate=True)
    def post(self):
        data = request.json
        return create_new_client(data=data)
