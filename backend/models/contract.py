from database import db

class Contract(db.Model):
    __tablename__ = 'contracts'
    id = db.Column(db.Integer, primary_key=True)
    contract_code = db.Column(db.String(50), nullable=False, unique=True)
    resident_id = db.Column(db.Integer, db.ForeignKey('residents.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    deposit = db.Column(db.Numeric(10, 2))
    status = db.Column(db.Enum('Active', 'Expired', 'Terminated'), default='Active')
