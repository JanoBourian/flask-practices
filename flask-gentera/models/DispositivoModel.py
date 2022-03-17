from time import timestamp

class DispositivoModel:
    
    def __init__(self, nombre_equipo:str = '', tipo_dispositivo_id:int=None, fecha_alta:timestamp=None, fecha_actualizacion:timestamp=None, potencia_actual:float=None, status_dispositivo_id:int=None)->None:
        self.nombre_equipo = nombre_equipo
        self.tipo_dispositivo_id = tipo_dispositivo_id
        self.fecha_alta = fecha_alta
        self.fecha_actualizacion = fecha_actualizacion
        self.potencia_actual = potencia_actual
        self.status_dispositivo_id = status_dispositivo_id
        