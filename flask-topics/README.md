# Playlist

https://www.youtube.com/playlist?list=PLeKKNy7-Y2sWC8tZ68TLgxpLvdeO0a9hW

# Repo

https://github.com/PythonistaMX/py221

# URL

```
<esquema>://<usuario>:<contraseña>@<anfitrión>:<puerto>/<ruta>?<consultas>
```

```
<esquema>://<anfitrión>:<puerto>/<ruta>?<consultas>
```

# Authentication

https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication

https://github.com/PythonistaMX/py241

```
https://www.google.com/search?q=pythonista

https://www.amazon.com/s?k=murakami
```

# Sniffers and auditory 

https://nmap.org/

https://www.wireshark.org/

https://scapy.net/

## Comandos 

```
app.config.from_file()
app.config.from_json() 
app.config.from_pyfile('settings.cfg')
```

# Type
- string
- int 
- float 
- path 
- uuid

# Jinja
- {{VAR}}
- {% <DECLARATION> %}
- {# COMMENT #}

# Jinja2
```
jinja2.FileSystemLoader('<ruta>')
jinja2.FileSystemLoader(['<ruta 1>', '<ruta 2>', ..., '<ruta n>'])
jinja2.Environment(loader = <objeto de la clase jinja2.FileSystemLoader>, <otros parámetros>)
```

## Example 

```
import os
import jinja2
from IPython.display import HTML 
miruta = os.getcwd()
entorno = jinja2.Environment(loader=jinja2.FileSystemLoader(miruta + '/plantillas'))
template = entorno.get_template("plantilla.html")
ligas = [['slashdot', 'https://slashdot.org'], 
         ['pythonista', 'https://pythonista.mx'], 
         ['cloudevel', 'https://cloudevel.com']]
print(template.render(lista=ligas))
HTML(template.render(lista=ligas))
```

## Aditional validations 

```
{% if numero is even %}
    <p> SOCIO </p>
{% elif numero is odd %}
    <p> ERROR </p>
{% endif %}
``` 

## Macros (little functions in her scope)

## WTForms

- https://wtforms.readthedocs.io/en/3.0.x/
- https://wtforms.readthedocs.io/en/2.3.x/fields/
- https://wtforms.readthedocs.io/en/2.3.x/validators/
- https://wtforms.readthedocs.io/en/2.3.x/widgets/

## FLASK_WTF

- https://flask-wtf.readthedocs.io/en/1.0.x/

## Flask request 

- http://flask.pocoo.org/docs/latest/api/#flask.Request

