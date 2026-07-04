from database import db

class Resident(db.Model):
    __tablename__ = 'residents'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    identity_card = db.Column(db.String(20), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date)
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(100))
    move_in_date = db.Column(db.Date)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    
    contracts = db.relationship('Contract', backref='resident', lazy=True)
