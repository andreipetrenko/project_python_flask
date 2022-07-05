from .. import db


class Deposits(db.Model):
    __tablename__ = 'deposits'

    dpst_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clnt_clnt_id = db.Column(db.Integer, db.ForeignKey('clients.clnt_id'))
    bank_bank_id = db.Column(db.Integer, db.ForeignKey('banks.bank_id'))
    deposite_amount = db.Column(db.Integer, nullable=False)
    date_open = db.Column(db.DateTime, nullable=False)
    date_close = db.Column(db.DateTime, nullable=True)
    date_update = db.Column(db.DateTime, nullable=True)
    procent = db.Column(db.Integer, nullable=True)
    month_deposit = db.Column(db.Integer, nullable=True)

    def __init__(self, dpst_id, clnt_clnt_id, deposite_amount, bank_bank_id, date_open, date_close, date_update, \
                 procent, month_deposit):
        self.dpst_id = dpst_id
        self.clnt_clnt_id = clnt_clnt_id
        self.bank_bank_id = bank_bank_id
        self.deposite_amount = deposite_amount
        self.date_open = date_open
        self.date_close = date_close
        self.date_update = date_update
        self.procent = procent
        self.month_deposit = month_deposit

    def __repr__(self):
        return '<Contributions %r>' % self.dpst_id % self.clnt_clnt_id % self.bank_bank_id % self.deposite_amount \
               % self.date_open % self.date_close % self.date_update % self.procent % self.month_contrib
