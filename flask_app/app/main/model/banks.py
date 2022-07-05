from .. import db


class Banks(db.Model):
    __tablename__ = 'banks'

    bank_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    bik = db.Column(db.Integer, nullable=False)

    def __init__(self, bank_id, name, bik):
        self.bank_id = bank_id
        self.name = name
        self.bik = bik

    def __repr__(self):
        return '<Banks %r>' % self.bank_id % self.name % self.bik
    