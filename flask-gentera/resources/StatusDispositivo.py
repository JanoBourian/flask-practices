from flask_restful import Resource, reqparse
import logging 

class StatusDispositivo(Resource):
    # parser
    parser = reqparse.RequestParser()
    # descripcion
    parser.add_argument("descripcion", type=str, required=True, help="descripcion es necesario")
    
    # Post
    def post(self):
        data = StatusDispositivo.parser.parse_args()
        try:
            descripcion = data.get('descripcion')
            
            # Validar que no exista otra descripcion igual
            
            # Agregar a la base de datos
            
            return {"Message": "This is OK!"}, 201
        except Exception as e:
            logging.warning(f"ERROR {e}")
    