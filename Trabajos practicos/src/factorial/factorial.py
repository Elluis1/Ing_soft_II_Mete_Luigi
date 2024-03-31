#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): # Crea la funcion para verificar el factorial
    if num == 0:
        return 1

    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

# Factorial numero unico
# num = 10 # Creamos el num
# num = int(input("Por favor, ingrese el numero a probar: "))

# if len(sys.argv) == 0:
#    print( "Debe informar un número!" );
#    sys.exit();
# else:
#     if num < 0:
#         print ("Los numeros negativos no tienen factorial")
#     elif num >= 0:
#         print("Factorial ",num,"! es ", factorial(num));
#     else:
#         print("Tiene que aportar el numero para hacer pruebas")
# Prueba el num y calcula el factorial

# Rangos con factoriales
# print("Ingrese los dos extremos: ")
# desde = int(input())
# hasta = int(input())

# if len(sys.argv) == 0:
#    print( "Debe informar un número!" );
#    sys.exit();
# else:
#     if desde | hasta  < 0:
#         print ("Los numeros negativos no tienen factorial")
#     elif desde & hasta >= 0:
#         print("El resultado de la multiplicacion de los factoriales es: ", (factorial(desde)*factorial(hasta)));
#     else:
#         print("Tiene que aportar el numero para hacer pruebas")

# Rangos de factoriales con minimo 1
# print("Ingrese el extremo mayor: ")
# num = 1
# hasta = int(input())

# if len(sys.argv) == 0:
#    print( "Debe informar un número!" );
#    sys.exit();
# else:
#     if hasta  < 0:
#         print ("Los numeros negativos no tienen factorial")
#     elif hasta >= 0:
#         print("El resultado de la multiplicacion de los factoriales es: ", (factorial(num)*factorial(hasta)));
#     else:
#         print("Tiene que aportar el numero para hacer pruebas")

# Rangos de factoriales con minimo 1
# print("Ingrese el extremo menor: ")
# num = 60
# desde = int(input())

# if len(sys.argv) == 0:
#    print( "Debe informar un número!" );
#    sys.exit();
# else:
#     if desde  < 0:
#         print ("Los numeros negativos no tienen factorial")
#     elif desde >= 0:
#         print("El resultado de la multiplicacion de los factoriales es: ", (factorial(num)*factorial(desde)));
#     else:
#         print("Tiene que aportar el numero para hacer pruebas")