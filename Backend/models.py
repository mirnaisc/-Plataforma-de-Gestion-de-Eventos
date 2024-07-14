from . import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)

class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    lugar = db.Column(db.String(128), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)

