# Process

    - Install all dependences

    - Initialize Basic Flask app
    
    - Use Flask-RESTful with Resource and Api and change View functions

    - Create the endpoints and resources without retrieve info:
        - Sketch the endpoints necessaries
        ```
        /
        /dispositivo <-POST->
        /lectura <-POST->
        /mantenimiento <-POST->
        /status <-POST->
        /tipo <-POST->
        /dispositivos <-GET->
        /dispositivo/id/<id:int> <-GET->
        /dispositivo/tipo/<id::int> <-GET->
        /lecturas <-GET->
        /lectura/dispositivo/id/<id:int> <-GET->
        /lectura/dispositivo/tipo/<tipo:str> <-GET->
        /energia <-GET->
        /energia/id <-GET->
        /mantenimietos <-GET->
        /mantenimiento/dispositivo/id/<id:int> <-GET->
        ```
        - For each one endpoint do the methods and validations

    - In this case I haved the class diagram for that I started with the models:
        - Create Class Model without SQLAlchemy implementation and without methods


# Install

```
pip install flask Flask-JWT-Extended Flask-RESTful Flask-SQLAlchemy Werkzeug flask-cors black python-dotenv
```