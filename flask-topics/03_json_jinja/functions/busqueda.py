def buscar_patron(patron, objeto, campos):
    for campo in campos:
        if patron.casefold() in objeto[campo].casefold():
            return True

def buscar_archivo(patron, ruta, campos):
    with open(ruta, 'tr') as file:
        base = eval(file.read())
        return [item for item in base if buscar_patron(patron, item, campos)]