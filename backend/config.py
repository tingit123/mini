import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-for-apartment-mini'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:123456789@localhost/apartment_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
