from database import db

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    amount = db.Column(db.Numeric(10, 2))
    expense_date = db.Column(db.Date)
    category = db.Column(db.String(50))
