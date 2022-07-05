from flask_restx import Namespace, fields


class ClientDto:
    api = Namespace('clients', description='client related operations')
    client = api.model('clients', {
        'clnt_id': fields.Integer(description='client identifier'),
        'name': fields.String(required=True, description='client name'),
        'short_name': fields.String(required=True, description='client short_name'),
        'address': fields.String(required=True, description='client address'),
        'jur_type': fields.Integer(description='client jur_type')
    })


class BankDto:
    api = Namespace('banks', description='banks list')
    bank = api.model('banks', {
        'bank_id': fields.Integer(description='bank identifier'),
        'name': fields.String(required=True, description='bank name'),
        'bik': fields.Integer(required=True, description='bik number')
    })


class DepositDto:
    api = Namespace('deposits', description='deposits list')
    deposit = api.model('deposits', {
        'dpst_id': fields.Integer(description='deposit identiier'),
        'clnt_clnt_id': fields.Integer(required=True, description='client identifier'),
        'bank_bank_id': fields.Integer(required=True, description='bank identifier'),
        'deposite_amount': fields.Integer(required=True, description='amount by deposite'),
        'date_open': fields.Date(required=True, description='date open deposite'),
        'date_close': fields.Date(required=True, description='date close deposite'),
        'date_update': fields.Date(required=True, description='date update deposite'),
        'procent': fields.Integer(required=True, description='procent by deposite'),
        'month_deposit': fields.Integer(required=True, description='month by deposite')
    })
