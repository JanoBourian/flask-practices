from datetime import datetime

class Lecturas:
    
    def __init__(self, id_dispositivo:int=None, id_tipo_dispositivo:int=None, potencia_actual:float=None, fecha_registro:datetime=None)->None:
        self.id_dispositivo = id_dispositivo
        self.id_tipo_dispositivo = id_tipo_dispositivo
        self.potencia_actual = potencia_actual
        self.fecha_registro = fecha_registro
        
        