import sys
import json

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-v":
        print("Version 1.1")
    else:
        print("Copyright UADERFCyT-IS2 ©2024 Todos los derechos reservados")

        # Solicitar al usuario que ingrese el nombre del archivo JSON y la clave
        jsonfile = input("Ingresa el nombre del archivo JSON: ")

        # Verificar si se proporcionó un nombre de archivo
        if jsonfile:
            jsonkey = input("Ingresa la clave del JSON: ")

            try:
                # Leer el contenido del archivo JSON
                with open(jsonfile, 'r') as myfile:
                    data = myfile.read()

                # Parsear el JSON
                obj = json.loads(data)

                # Generar el objeto
                objarchivo = {
                    jsonfile: obj.get(jsonkey, "La clave no existe en el JSON"),
                }

                print("El objeto del archivo es:", objarchivo)
            except FileNotFoundError:
                print("El archivo especificado no se encontró.")
            except Exception as e:
                print("Ocurrió un error:", e)
        else:
            print("No se proporcionó un nombre de archivo.")

if __name__ == "__main__":
    main()
