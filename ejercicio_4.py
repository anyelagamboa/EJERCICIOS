"""
40.Un triángulo se puede clasificar según la longitud de sus lados como equilátero, 
isósceles o escaleno. Los 3 lados de un triángulo equilátero tienen la misma longitud. 
Un triángulo isósceles tiene dos lados que tienen la misma longitud y un tercer lado 
que tiene una longitud diferente. Si todos los lados tienen diferentes longitudes, 
entonces el triángulo es escaleno. Escriba un programa que lea las longitudes de
3 lados de un triángulo del usuario. Mostrar un mensaje indicando el tipo de triángulo
"""

def triangulo(lado_1,lado_2,lado_3):
    if (lado_1 == lado_2 or lado_1==lado_3):
        if (lado_2==lado_3):
            return "EQUILATERO"
        else:
            return"ISOCELES"
    elif(lado_2==lado_3):
        return "ISOCELES"
    else:
        return "ESCALENO"
    
lado_1=int(input("Ingrese la longitud del primer lado: "))
lado_2=int(input("Ingrese la longitud del segundo lado: "))
lado_3=int(input("Ingrese la longitud del tercer lado: "))
print("El triangulo es ",triangulo(lado_1,lado_2,lado_3))