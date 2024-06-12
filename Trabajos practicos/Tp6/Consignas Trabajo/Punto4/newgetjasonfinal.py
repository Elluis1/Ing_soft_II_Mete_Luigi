import sys
import json
import os

# Clase para representar un pago
class Pago:
    def __init__(self, numero_pedido, banco, monto):
        self.numero_pedido = numero_pedido
        self.banco = banco
        self.monto = monto

    def __str__(self):
        return f"Pedido #{self.numero_pedido}: Banco {self.banco} - Monto: ${self.monto}"

# Clase para gestionar los pagos
class GestorPagos:
    def __init__(self):
        self.pagos_realizados = []
        self.numero_pedido = 1

    def realizar_pago(self, banco, monto):
        pago = Pago(self.numero_pedido, banco, monto)
        self.pagos_realizados.append(pago)
        self.numero_pedido += 1

    def listar_pagos(self):
        return iter(self.pagos_realizados)

# Función para cargar los datos de los bancos desde un archivo JSON
def load_banks(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []

# Función para mostrar los bancos disponibles
def show_banks(bancos):
    print("Bancos disponibles:")
    for i, banco in enumerate(bancos, 1):
        print(f"{i}. {banco['nombre']} - Saldo: ${banco['saldo']}")

# Función para seleccionar un banco y realizar el pago de manera balanceada
def select_bank(bancos, gestor_pagos):
    coste = 500
    for banco in bancos:
        if banco["saldo"] >= coste:
            banco["saldo"] -= coste
            gestor_pagos.realizar_pago(banco["nombre"], coste)
            print(f"Pedido #{gestor_pagos.numero_pedido - 1} realizado con el banco {banco['nombre']} por un monto de ${coste}.")
            return
    print("No se encontró ningún banco con saldo suficiente.")

# Función principal del programa
def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-v":
        print("Versión 1.2")
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

                # Cargar los datos del archivo JSON
                bancos = load_banks(jsonfile)

                # Verificar que se han cargado bancos
                if not bancos:
                    print("No se encontraron bancos en el archivo JSON.")
                    return

                # Mostrar bancos disponibles
                show_banks(bancos)

                # Crear un gestor de pagos
                gestor_pagos = GestorPagos()

                # Realizar pagos de forma balanceada
                while True:
                    select_bank(bancos, gestor_pagos)
                    continuar = input("¿Deseas realizar otro pago? (s/n): ")
                    if continuar.lower() != 's':
                        break

                # Listar todos los pagos realizados
                print("\nPagos realizados:")
                for pago in gestor_pagos.listar_pagos():
                    print(pago)

            except FileNotFoundError:
                print("El archivo especificado no se encontró.")
            except Exception as e:
                print("Ocurrió un error:", e)
        else:
            print("No se proporcionó un nombre de archivo.")

if __name__ == "__main__":
    main()
