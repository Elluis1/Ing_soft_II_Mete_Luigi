import sys
import json
import os

# b) En realidad el proceso de decisión se puede automatizar, bastará que exista
# saldo en la respectiva cuenta y que los pagos se hagan en forma balanceada

def load_banks(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo '{archivo}' no se encontró.")
        return{}
    except Exception as e:
        print(f"ocurrio un error al leer el archivo: {e}")
        return{}

def show_banks(bancos):
    print("Bancos disponibles: ")
    for i, (banco) in enumerate(bancos, 1):
        print(f"{i}. {banco}")

# def select_bank(bancos):
#     while True:
#         try:
#             seleccion = int(input("Selecciona el numero del banco:"))
#             if 1 <= seleccion <= len(bancos):
#                 banco_seleccionado = list(bancos.keys())[seleccion - 1]
#                 return banco_seleccionado, bancos[banco_seleccionado]
#             else:
#                 print("seleccion invalida, intenta de nuevo.")
#         except ValueError:
#             print("Entrada invalida, por favor ingresa un numero")


def select_bank(bancos):
        try:
            coste = int(input("¿Cuanto es el coste del pago? "))
            if 1 <= coste:
                for i in bancos:
                    if i["saldo"] >= coste:
                        return print("este token realiza el pago", i["nombre"])
                    else:
                        return print("No tenes ningun token que pueda costearlo")
            else:
                print("coste invalido, intenta de nuevo.")
        except ValueError:
            print("Entrada invalida, por favor ingresa un numero")

def token_validation(token_correcto, token_ingresado):
    return token_correcto == token_ingresado


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-v":
        print("Version 1.1")
    else:
        print("Copyright UADERFCyT-IS2 ©2024 Todos los derechos reservados")

        # Solicitar al usuario que ingrese el nombre del archivo JSON
        jsonfile = input("Ingresa el nombre del archivo JSON: ")

        # Verificar si se proporcionó un nombre de archivo
        if jsonfile:
            try:
                # Verificar si el archivo se encuentra en el directorio
                if not os.path.isfile(jsonfile):
                    raise FileNotFoundError

                # Leer el contenido del archivo JSON
                with open(jsonfile, 'r') as myfile:
                    data = myfile.read()

                # Parsear el JSON
                obj = json.loads(data)

                # Generar el objeto
                objarchivo = {
                    jsonfile: obj,
                }

                print("El objeto del archivo es:", json.dumps(objarchivo, indent=4, ensure_ascii=False))

                # Nuevas funcionalidades: selección de banco y validación de token
                bancos = obj
                if not bancos:
                    return

                show_banks(bancos)
                banco_seleccionado = select_bank(bancos)

            except FileNotFoundError:
                print("El archivo especificado no se encontró.")
            except Exception as e:
                print("Ocurrió un error:", e)
        else:
            print("No se proporcionó un nombre de archivo.")

if __name__ == "__main__":
    main()
