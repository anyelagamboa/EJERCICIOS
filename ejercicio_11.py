"""
75.l máximo común divisor de dos números enteros positivos, n y m, es el número más grande, d, que se divide 
por igual entre n y m. Hay varios algoritmos que se pueden utilizar para resolver este problema, entre ellos:
Inicializar d al menor de m y n.
Mientras que d no divide uniformemente m o d no divide uniformemente n do
Disminuye el valor de d en 1
Reporte d como el máximo común divisor de n y m
Escriba un programa que lea dos enteros positivos del usuario y use este algoritmo para determinar y 
reportar su máximo común divisor.
"""


def maximoComunDivisor(numero_1, numero_2):
    aux = 0
    while numero_2 != 0 and numero_2<0:
        aux = numero_2
        numero_2 = numero_1 % numero_2
        numero_2 = aux
    return numero_2


numero_1=int(input("Ingrese un numero: "))
numero_2=int(input("Ingrese un numero: "))
print(maximoComunDivisor(numero_1,numero_2))