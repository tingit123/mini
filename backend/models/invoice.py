from database import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rent_amount = db.Column(db.Numeric(10, 2))
    electricity_amount = db.Column(db.Numeric(10, 2))
    water_amount = db.Column(db.Numeric(10, 2))
    service_fee = db.Column(db.Numeric(10, 2))
    total_amount = db.Column(db.Numeric(10, 2))
    status = db.Column(db.Enum('Unpaid', 'Paid'), default='Unpaid')
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    payments = db.relationship('Payment', backref='invoice', lazy=True)
