import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:123456789@localhost:5432/BD_Gestion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
