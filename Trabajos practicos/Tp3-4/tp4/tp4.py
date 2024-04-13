import subprocess
from proxy import *
import re

IP = '192.168.0.254'

class Ping:
    def __init__(self):
        pass

    def execute(self, port):
        if not re.match(r'^192\.', port):
            print('La direccion IP no comienza con 192., es obligatorio ')
            return

        for i in range(10):
            try:
                result = subprocess.run(['ping', '-c', '1', port], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5, universal_newlines=True)
                if result.returncode == 0:
                    print(f"Ping exitoso a {port}")
                else:
                        print(f"Intento {i+1}: No se pudo hacer ping a {port}")
            except subprocess.TimeoutExpired:
                    print(f"Intento {i+1}: Tiempo de espera agotado para {port}")
            except Exception as e:
                    print(f"Error al intentar hacer ping a {port}: {str(e)}")


    def executeFree(self, ip_address):
        # Realizar 10 intentos de ping sin verificación de dirección
        for i in range(3):
            try:
                result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5, universal_newlines=True)
                if result.returncode == 0:
                    print(f"Ping exitoso a {ip_address}")
                else:
                    print(f"Intento {i+1}: No se pudo hacer ping a {ip_address}")
            except subprocess.TimeoutExpired:
                print(f"Intento {i+1}: Tiempo de espera agotado para {ip_address}")
            except Exception as e:
                print(f"Error al intentar hacer ping a {ip_address}: {str(e)}")


ping = Ping()
# ping.execute('192.168.1.1')
ping.executeFree('132.168.1.1')