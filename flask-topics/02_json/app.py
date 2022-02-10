import json 

estudiante = {'nombre': ['Juan', 'Pérez', 'Sánchez'], 'rol':'estudiante'}
print(json.dumps(estudiante))
nuevo_estudiante = json.loads(json.dumps(estudiante))
print(nuevo_estudiante)

## for files json.dump() y json.load()

with open("alumno.json", "wt") as file: 
    json.dump(estudiante, file)

with open("alumno.json", "rt") as archivo:
    otro_estudiante = json.load(archivo)

print(estudiante == otro_estudiante)