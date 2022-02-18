from db import db
import logging

class MovimentModel(db.Model):
    
    __tablename__ = 'moviments'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Float(precision=2), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    concepto = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    
    def __init__(self, cantidad, tipo, concepto, fecha):
        self.cantidad = cantidad
        self.tipo = tipo
        self.concepto = concepto
        self.fecha = fecha
    
    def add_to_database(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logging.warning(f"ERROR: {e}")
    
    @classmethod
    def get_all_elements(cls):
        try:
            items = cls.query.all()
            return items
        except Exception as e:
            logging.warning(f"ERROR: {e}")