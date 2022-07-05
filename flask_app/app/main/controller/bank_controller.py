from flask import request
from flask_restx import Resource

from ..unit.dto import BankDto
from ..service.banks_service import create_new_bank, get_all_banks

api = BankDto.api
_bank = BankDto.bank


@api.route('/all')
class GetBanks(Resource):
    @api.doc('list of banks')
    @api.marshal_list_with(_bank, envelope='data')
    def get(self):
        return get_all_banks()


@api.route('/create')
class PostBank(Resource):
    @api.response(201, 'Bank create success!')
    @api.doc('create a new bank')
    @api.expect(_bank, validate=True)
    def post(self):
        data = request.json
        return create_new_bank(data=data)
