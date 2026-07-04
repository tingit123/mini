from database import db

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(20), nullable=False, unique=True)
    floor = db.Column(db.Integer)
    area = db.Column(db.Float)
    rent_price = db.Column(db.Numeric(10, 2))
    status = db.Column(db.Enum('Available', 'Rented', 'Maintenance'), default='Available')
    
    residents = db.relationship('Resident', backref='room', lazy=True)
    contracts = db.relationship('Contract', backref='room', lazy=True)
    electricity_waters = db.relationship('ElectricityWater', backref='room', lazy=True)
    invoices = db.relationship('Invoice', backref='room', lazy=True)
