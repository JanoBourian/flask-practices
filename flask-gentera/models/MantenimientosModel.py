from datetime import datetime

class Mantenimientos:
    
    def __init__(self, id_dispositivo:int=None, id_tipo_dispositivo:int = None, disponible:bool = None, fecha_registro:datetime=None)->None:
        self.id_dispositivo = id_dispositivo
        self.id_tipo_dispositivo = id_tipo_dispositivo
        self.disponible = disponible
        self.fecha_registro = fecha_registro
        