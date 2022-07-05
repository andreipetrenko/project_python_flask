from flask import request
from flask_restx import Resource

from ..unit.dto import DepositDto
from ..service.deposits_service import create_new_deposit

api = DepositDto.api
_deposit = DepositDto.deposit


@api.route('/create')
class PostBank(Resource):
    @api.response(201, 'Deposit create success!')
    @api.doc('create a new deposit')
    @api.expect(_deposit, validate=True)
    def post(self):
        data = request.json
        return create_new_deposit(data=data)
