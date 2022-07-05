from app.main import db
from app.main.model.deposits import Deposits


def create_new_deposit(data):
    new_contribution = Deposits(
        dpst_id=data['dpst_id'],
        clnt_clnt_id=data['clnt_clnt_id'],
        bank_bank_id=data['bank_bank_id'],
        deposite_amount=data['deposite_amount'],
        date_open=data['date_open'],
        date_close=data['date_close'],
        date_update=data['date_update'],
        procent=data['procent'],
        month_deposit=data['month_deposit']
    )
    save_changes(new_contribution)
    responce_body = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return responce_body, 201


def save_changes(data):
    db.session.add(data)
    db.session.commit()
