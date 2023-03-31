"""
81.Escribe una función que tome las longitudes de los dos lados más cortos de un triángulo 
rectángulo como sus parámetros. Devuelve la hipotenusa del triángulo, calculada mediante 
el teorema de Pitágoras, como resultado de la función. Incluya un programa principal que 
lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, 
use su función para calcular la longitud de la hipotenusa y muestre el resultado.
"""
import math
def TeoremaPitagoras(lado_1,lado_2):
    hipotenusa= math.sqrt((lado_1*lado_1)+(lado_2*lado_2))
    return hipotenusa

lado_1=float(input("Lado 1: "))
lado_2=float(input("Lado 2: "))

print("La hipotenusa es ",TeoremaPitagoras(lado_1,lado_2))