import json

# Solicitar al usuario que ingrese el nombre del archivo JSON y la clave
jsonfile = input("Ingresa el nombre del archivo JSON: ")
jsonkey = input("Ingresa la clave del JSON: ")

# Leer el contenido del archivo JSON
with open(jsonfile, 'r') as myfile:
    data = myfile.read()

# Parsear el JSON
obj = json.loads(data)

# Imprimir el valor correspondiente a la clave especificada
print(obj.get(jsonkey, "La clave no existe en el JSON"))