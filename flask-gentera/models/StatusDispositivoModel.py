from db import db
import logging 

class StatusDispositivoModel(db.Model):
    
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(50), unique = True, nullable = False)
    
    def __init__(self, descripcion:str = '')->None:
        self.descripcion = descripcion