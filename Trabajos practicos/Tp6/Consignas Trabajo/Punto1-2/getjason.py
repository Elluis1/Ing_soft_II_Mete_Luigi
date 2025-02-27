import json

def leer_json(archivo):
    """
    Lee un archivo JSON y devuelve los datos en un objeto.

    :param archivo: Ruta al archivo JSON.
    :return: Objeto con los datos del archivo JSON.
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo {archivo}.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    archivo = 'sitedata.json'
    datos = leer_json(archivo)
    if datos:
        print(datos)

