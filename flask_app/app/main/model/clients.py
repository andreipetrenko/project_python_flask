from .. import db


class Clients(db.Model):

    __tablename__ = 'clients'

    clnt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    short_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    jur_type = db.Column(db.Integer, nullable=False)

    def __init__(self, clnt_id, name, short_name, address, jur_type):
        self.clnt_id = clnt_id
        self.name = name
        self.short_name = short_name
        self.address = address
        self.jur_type = jur_type

    def __repr__(self):
        return '<User %r>' % self.clnt_id % self.name % self.short_name % self.address % self.jur_type
