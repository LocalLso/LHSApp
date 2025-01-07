import os

class Config:
    SECRET_KEY = '54b2e5710499e63a978c254e45e609708f098be9d79fdb04'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
