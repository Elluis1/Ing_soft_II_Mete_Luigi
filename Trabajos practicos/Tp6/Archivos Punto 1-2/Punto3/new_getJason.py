import json

print("copyright UADERFCyT-IS2©2024 todos los derechos reservados")

# Solicitar al usuario que ingrese el nombre del archivo JSON y la clave
jsonfile = input("Ingresa el nombre del archivo JSON: ")
jsonkey = input("Ingresa la clave del JSON: ")

# Creando el error del codigo no de la maquina
if jsonfile == True:
    # Leer el contenido del archivo JSON
    with open(jsonfile, 'r') as myfile:
        data = myfile.read()

    # Parsear el JSON
    obj = json.loads(data)

    # Generar el objeto
    objArchivo = {
        jsonfile,
        obj.get(jsonkey, "La clave no existe en el JSON"),
    }

    print("El objeto del archivo es: ", objArchivo)
else:
    print("Error")



# # Imprimir el valor correspondiente a la clave especificada
# print(obj.get(jsonkey, "La clave no existe en el JSON"))