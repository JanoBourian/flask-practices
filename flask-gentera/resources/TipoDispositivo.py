from flask_restful import Resource, reqparse
import logging

class TipoDispositivo(Resource):
    # reqparse
    parser = reqparse.RequestParser()
    # nombre_tipo
    parser.add_argument("nombre_tipo", type=str, required=True, help="nombre_tipo es requerido")
    
    # Post
    def post(self):
        data = TipoDispositivo.parser.parse_args()
        try:
            nombre_tipo = data.get('nombre_tipo')
            
            # Validar que no exista otro nombre tipo
            
            # Agregar a la base de datos
            
            return {"Message": "All OK!"}, 201
        except Exception as e:
            logging.warning(f"ERROR {e}")