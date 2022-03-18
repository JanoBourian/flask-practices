from flask_restful import Resource, reqparse
from datetime import datetime
from models import MantenimientosModel
import logging

class Mantenimiento(Resource):
    # reqparse
    reqparser = reqparse.RequestParser()
    # id_dispositivo
    reqparser.add_argument("id_dispositivo", type=int, required=True, help="id_dispositivo es necesario")
    # id_tipo_dispositivo
    reqparser.add_argument("id_tipo_dispositivo", type=int, required=True, help="id_tipo_dispositivo es necesario")
    
    # Post
    def post(self):
        data = Mantenimiento.reqparser.parse_args()
        try:
            id_dispositivo = data.get('id_dispositivo')
            id_tipo_dispositivo = data.get('id_tipo_dispositivo')
            # validar existencia de id_dispositivo
            # validar existencia de id_tipo_dispositivo
            # agregar a la base de datos            
        except Exception as e:
            logging.warning(f"ERROR: {e}")