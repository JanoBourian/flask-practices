# Process
    - Install all dependences
    - Initialize Basic Flask app
    - Use Flask-RESTful with Resource and Api and change View functions
    - Create the endpoints and resources without retrieve info:
        - Sketch the endpoints necessaries
        ```
        /
        /dispositivos 
        /dispositivo/id/<id:int>
        /dispositivo/tipo/<id::int>
        /lecturas
        /lectura/dispositivo/id/<id:int>
        /lectura/dispositivo/tipo/<tipo:str>
        /energia
        /energia/id
        /mantenimietos
        /mantenimiento/dispositivo/id/<id:int>
        ```
    - In this case I haved the class diagram for that I started with the models:
        - Create Class Model without SQLAlchemy implementation and without methods


# Install

```
pip install flask Flask-JWT-Extended Flask-RESTful Flask-SQLAlchemy Werkzeug flask-cors black python-dotenv
```