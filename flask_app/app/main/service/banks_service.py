from app.main import db
from app.main.model.banks import Banks


def create_new_bank(data):
    new_bank = Banks(
        bank_id=data['bank_id'],
        name=data['name'],
        bik=data['bik']
    )
    save_changes(new_bank)
    responce_body = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return responce_body, 201


def get_all_banks():
    return Banks.query.all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
