from datetime import datetime
from db import db
import logging

class Mantenimientos(db.Model):
    
    __tablename__ = 'mantenimientos'
    id = db.Column(db.Integer, primary_key=True)
    id_dispositivo = db.Column(db.Integer, nullable=False)
    id_tipo_dispositivo = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, id_dispositivo:int=None, id_tipo_dispositivo:int = None)->None:
        self.id_dispositivo = id_dispositivo
        self.id_tipo_dispositivo = id_tipo_dispositivo
        self.fecha_registro = datetime.now()
        