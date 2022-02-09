def html(funcion):
    def etiquetas(texto):
        return f"<h1> {texto} </h1>"
    return etiquetas

@html
def parrafo(texto):
    return f"<p> {texto} </p>"

print(parrafo("Hola Mundo"))
