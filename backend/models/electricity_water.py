from database import db

class ElectricityWater(db.Model):
    __tablename__ = 'electricity_water'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    old_electricity = db.Column(db.Integer)
    new_electricity = db.Column(db.Integer)
    electricity_price = db.Column(db.Numeric(10, 2))
    old_water = db.Column(db.Integer)
    new_water = db.Column(db.Integer)
    water_price = db.Column(db.Numeric(10, 2))
    recorded_date = db.Column(db.Date)
