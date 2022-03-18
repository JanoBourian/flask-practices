from db import db
import logging 

class TiposDispositivoModel(db.Model):
    
    __tablename__ = 'tiposdispositivo'
    id = db.Column(db.Integer, primary_key=True)
    nombre_tipo = db.Column(db.String(50), unique = True, nullable = False)
    
    def __init__(self, nombre_tipo:str = '' )->None:
        self.nombre_tipo = nombre_tipo
    
    