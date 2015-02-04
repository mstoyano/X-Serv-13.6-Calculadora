#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

"""

Programa que sirve de calculadora e incluye las funciones básica
(sumar (+), restar (-), multiplicar (\*) y dividir (/)). 
Para ejecutar el programa:
$ python calculadora.py función operando1 operando2

"""
try:
    if len(sys.argv) == 4:
        op = sys.argv[1]
        op1 = sys.argv[2]
        op2 = sys.argv[3]
    else:
        raise IndexError

except IndexError:
    print 'Utiliza: $ python calculadora.py función operando1 operando2'
    print 
    sys.exit()

def suma(x, y):
    """Funcion que suma dos variables"""
    return x + y

def resta(x, y):
    """Funcion que resta dos variables"""
    return x - y

def multiplicacion(x, y):
    """Funcion que multiplica dos variables"""
    return x * y

def division(x, y):
    """Funcion que divide dos variables"""
    return x / y

if __name__ == "__main__":

    if op is '+':
        print 'Resultado: ' + str(suma(float(op1), float(op2)))
    elif op is '-':
        print 'Resultado: ' + str(resta(float(op1), float(op2)))
    elif op is '*':
        print 'Resultado: ' + str(multiplicacion(float(op1), float(op2)))
    elif op is '/':
        try:
            print 'Resultado: ' + str(division(float(op1), float(op2)))
        except ZeroDivisionError:
            print 'Intentas dividir por cero'
    else:
        print 'El operador no es valido'
