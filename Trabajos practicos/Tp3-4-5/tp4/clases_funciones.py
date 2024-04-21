import subprocess
from proxy import *
import re
from bridge import *
from composite import *

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

class PingProxy:
    def __init__(self):
         self.ping = Ping()

    def execute(self, port):
        if port == '192.168.0.254':
            self.ping.executeFree("www.google.com")
        else:
            self.ping.execute(port)

class NumberOperations:
    def __init__(self, number):
        self.number = number

    def get_value(self):
        return self.number


class NumberDecorator(NumberOperations):
    def __init__(self, component):
        self._component = component

    def get_value(self):
        return self._component.get_value()


class AddTwoDecorator(NumberDecorator):
    def get_value(self):
        return self._component.get_value() + 2


class MultiplyByTwoDecorator(NumberDecorator):
    def get_value(self):
        return self._component.get_value() * 2


class DivideByThreeDecorator(NumberDecorator):
    def get_value(self):
        return self._component.get_value() / 3

class laminasFabric():
    def punto2(opcion):
        if opcion == 1:

            implementation = ConcreteImplementationC()
            abstraction = Abstraction(implementation)
            client_code(abstraction)

            print("\n")
        elif opcion == 2:
            implementation = ConcreteImplementationD()
            abstraction = ExtendedAbstraction(implementation)
            client_code(abstraction)

            print("\n")
        else:
            print("Esa no es una opcion")

class subConjuntos():
    def punto4():
        tree = Composite()
        rama1 = Composite()
        rama1.add(Leaf())
        rama1.add(Leaf())
        rama1.add(Leaf())
        rama1.add(Leaf())

        rama2 = Composite()
        rama2.add(Leaf())
        rama2.add(Leaf())
        rama2.add(Leaf())
        rama2.add(Leaf())

        rama3 = Composite()
        rama3.add(Leaf())
        rama3.add(Leaf())
        rama3.add(Leaf())
        rama3.add(Leaf())

        tree.add(rama1)
        tree.add(rama2)
        tree.add(rama3)

        client_code(tree)