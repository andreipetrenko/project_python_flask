from app.main import db
from app.main.model.clients import Clients


def create_new_client(data):
    # client = Clients.query.filter_by(email=data['email']).first()
    # added data in client table
    new_client = Clients(
        clnt_id=data['clnt_id'],
        name=data['name'],
        short_name=data['short_name'],
        address=data['address'],
        jur_type=data['jur_type']
    )
    save_changes(new_client)
    responce_body = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return responce_body, 201


def get_all_clients():
    return Clients.query.all()


def get_client_by_id(clnt_id):
    return Clients.query.filter_by(clnt_id=clnt_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
