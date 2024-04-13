from builder import *
from prototype import SomeComponent, SelfReferencingEntity, copy, time

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# funcion punto 1 ( factorial )
def factorial (num, metaclass=Singleton):
    a = 1
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return 'Los numeros negativos no tienen factorial'
    else:
        while num > 1:
            a *= num
            num -= 1
        return a

# funcion punto 2 ( impuestos )
def calculoImpuestos(valor):
    if valor <= 0:
        return 'No hay nada que calcular'

    else:
        impuesto_1 = valor * 0.21
        impuesto_2 = valor * 0.05
        impuesto_3 = valor * 0.012

        total_impuestos = impuesto_1 + impuesto_2 + impuesto_3
        total_a_pagar = valor + total_impuestos

        return total_a_pagar

# funcion punto 3 ( "hamburguesa" )
def entregaFastFood(entrega):
    if entrega == 1:
        return 'La entrega se realizo por mostrador'
    elif entrega == 2:
        return 'La hamburguesa la retira el cliente'
    elif entrega == 3:
        return 'La hamburguesa es enviada por delivery'
    else:
        return 'No es una forma de entrega'

# funcion punto 4 ( "Factura" )
def condicionIVA(condicion):

    if condicion == 1: # Crea la factura si es IVA Responsable
        print('               Factura                     ')
        print('                                           ')
        print('Su condicion impositiva es: IVA Responsable')
        print('                                           ')
        print('                                           ')

    elif condicion == 2: # Crea la factura si es IVA no inscripto
        print('                Factura                     ')
        print('                                            ')
        print('Su condicion impositiva es: IVA no inscripto')
        print('                                            ')
        print('                                            ')

    elif condicion == 3: # Crea la factura si es IVA Exento
        print('               Factura                     ')
        print('                                           ')
        print('  Su condicion impositiva es: IVA Exento   ')
        print('                                           ')
        print('                                           ')

    else:
        return 'No es una condicion impositiva'

# funcion punto 5 ( "avión" )
def crearAvion():
    builder = ConcreteBuilder1()

    builder.produce_part_body()
    builder.produce_part_ala()
    builder.produce_part_turbinas()
    builder.produce_part_tren()
    builder.product.list_parts()

# punto 6 ( "Anidamientos" )
def espera2Seg():
    print("Simulando proceso de 2 segundos...")
    time.sleep(2)
    print("Proceso completado.")

def espera1Seg():
    time.sleep(1)

def llamadoFunciones():
    # punto 1
    print('')
    print('Punto 1')
    print('Escriba el numero del que quiere saber el factorial: ')
    print('Factorial: ', factorial(int(input())))
    espera1Seg()

    # punto 2
    print('')
    print('Punto 2')
    print('Ingrese el valor del que quiere recibir el calculo: ')
    print('Resultado del calculo: ', calculoImpuestos(int(input())))
    espera1Seg()

    # punto 3 (Lo hice por numeros para simplificar)
    print('')
    print('Punto 3')
    print('De que manera quiere la entrega(1 = mostrador, 2 = retira el cliente, 3 = delivery): ')
    print(entregaFastFood(int(input())))
    espera1Seg()

    # punto 4
    print('')
    print('Punto 4')
    print('¿Que condicion impositiva tiene usted?(1 = IVA Responsable, 2 = IVA no inscripto, 3 = IVA Exento): ')
    print(condicionIVA(int(input())))
    espera1Seg()

    # punto 5
    print('')
    print('Punto 5')
    print('Creacion de un avion:')
    espera1Seg()
    print(crearAvion())
    print('')

