from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bank(db.Model):
    __tablename__ = 'banks'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(49), nullable=True)

class Branch(db.Model):
    __tablename__ = 'branches'
    ifsc = db.Column(db.String(11), primary_key=True)
    bank_id = db.Column(db.BigInteger, db.ForeignKey('banks.id'), nullable=True)
    branch = db.Column(db.String(74), nullable=True)
    address = db.Column(db.String(195), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    district = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
