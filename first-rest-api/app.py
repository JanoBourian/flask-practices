from logging import exception
from flask import (Flask , jsonify, request)

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store', 
        'items' : [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]

# POST
# GET
# PUT
# DELETE

# POST /store data: {name: }
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    print(request_data)
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name:str): # '/store/some_name
    try:
        for store in stores:
            if store['name'] == name:
                return jsonify(store), 200
        return jsonify({"error": "Elemento no encontrado"}), 200      
    except Exception as e: 
        return jsonify({"error":f"{e}"}), 500

# GET /store
@app.route('/store', methods=['GET'])
def get_store_list():
    print(stores)
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def post_item_store(name:str): # '/store/some_name
    try:
        for store in stores:
            print(store)
            if store['name'] == name: 
                data = request.get_json()
                item ={
                    "name": data['name'],
                    "price": data['price']
                }
                store['items'].append(item)
                return jsonify(item), 200
        return jsonify({"message": "Store Not Found"}), 200     
    except Exception as e: 
        return jsonify({"error":f"{e}"}), 500

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_store(name:str): # '/store/some_name
    try:
        for store in stores:
            if store['name'] == name: 
                return jsonify({'items': store['items']})
        return jsonify({"error": "Elemento no encontrado"}), 200      
    except Exception as e: 
        return jsonify({"error":f"{e}"}), 500

@app.route('/')
def home():
    return '<h1> Hello, world! </html>'

if __name__ == '__main__':
    host = '127.0.0.1'
    port = '5000'
    debug = True
    app.run(host = host, port = port, debug = debug)