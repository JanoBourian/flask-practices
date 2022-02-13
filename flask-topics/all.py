def html(funcion):
    def etiquetas(texto):
        return f"<h1> {texto} </h1>"
    return etiquetas

@html
def parrafo(texto):
    return f"<p> {texto} </p>"

print(parrafo("Hola Mundo"))

def encuentra(patron, obj, campos):
    resultado = []
    for campo in campos: 
        resultado.append(patron.casefold() in obj[campo].casefold())
    return sum(resultado)

patron = 'n'
obj = {
    'nombre': 'Juan',
    'apellido': 'Godinez',
    'correo': 'falsoner@falso.com'
}
campos = ['nombre', 'apellido', 'correo']

res = encuentra(patron = patron, obj = obj, campos = campos)
print(res)