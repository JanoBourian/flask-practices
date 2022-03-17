from flask_restful import Resource, reqparse
import logging 
from datetime import datetime

class Dispositivo(Resource):
    # parser 
    parser = reqparse.RequestParser()
    # nombre_equipo
    parser.add_argument("nombre_equipo", type=str, required=True, help="nombre_equipo es necesario")
    # tipo_dispositivo_id
    parser.add_argument("tipo_dispositivo_id", type=int, required=True, help="tipó_dispositivo_id es necesario")
    # potencia_actual
    parser.add_argument("potencia_actual", type=float, required=True, help="potencia_actual es necesaria")
    # status_dispositivo_id
    parser.add_argument("status_dispositivo_id", type=int, required=True, help="status_dispositivo_id es necesario")
    
    # Post
    def post(self):
        data = Dispositivo.parser.parse_args()
        try:
            nombre_equipo = data.get("nombre_equipo")
            tipo_dispositivo_id = data.get("tipo_dispositivo_id")
            fecha_alta = datetime.now()
            fecha_actualizacion = datetime.now()
            potencia_actual = data.get("potencia_actual")
            status_dispositivo_id = data.get("status_dispositivo_id")
            
            # Buscar que no exista el nombre_equipo
            
            # Buscar que no exista el tipo_dispositivo_id
            
            # Buscar que no exista el status_dispositivo_id
            
            # Agregar a la base de datos
            return {"Message":"Consulta OK!"}, 201
            
        except Exception as e:
            logging.warning(f"ERROR {e}")
            
            
    # Put
    
    
    
    
    # Delete