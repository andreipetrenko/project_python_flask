from flask_restx import Api
from flask import Blueprint

from .main.controller.client_controller import api as clnt_ns
from .main.controller.bank_controller import api as bank_ns
from .main.controller.deposit_controller import api as deposit_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(clnt_ns, path='/client')
api.add_namespace(bank_ns, path='/bank')
api.add_namespace(deposit_ns, path='/deposit')
