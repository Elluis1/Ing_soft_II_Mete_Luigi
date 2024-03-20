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

if len(sys.argv) == 0:
   print( "Debe informar un número!" );
   sys.exit();
# En caso que la persona no aporte el numero

num = 10 # Creamos el num

if num < 0:
    print ("Los numeros negativos no tienen factorial")
else:
    print("Factorial ",num,"! es ", factorial(num));
# Prueba el num y calcula el factorial

# pruebas
