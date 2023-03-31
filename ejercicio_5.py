"""
45.Las posiciones en un tablero de ajedrez se identifican con una letra y un número.
La letra identifica la columna, mientras que el número identifica la fila, como se muestra a continuación:

Escriba un programa que lea una posición del usuario. 
Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 
Luego usa la aritmética modular para informar el color del cuadrado en esa fila. 
Por ejemplo, si el usuario ingresa a1, su programa debería informar que el cuadrado es negro. 
Si el usuario ingresa d5, su programa debe informar que el cuadrado es blanco. Su programa puede suponer 
que siempre se ingresará una posición válida. No es necesario realizar ninguna comprobación de errores.
"""

def ajedrez (letra,numero):
    if letra=="a" or letra=="c" or letra=="e" or letra=="g" or\
        letra=="A" or letra=="C" or letra=="E" or letra=="G":
        if (numero>0 and numero<9):
            if(numero%2==0):
                return "El cuadro es blanco"
            else:
                return "El cuadro es negro "
        else:
            return "Error solo valores de 1 a 8"
    elif letra=="b" or letra=="d" or letra=="f" or letra=="h" or\
        letra=="B" or letra=="D" or letra=="F" or letra=="H":
        if (numero>0 and numero<9):
            if(numero%2!=0):
                return "El cuadro es blanco"
            else:
                return "El cuadro es negro "
        else:
            return "Error solo valores de 1 a 8"
    else:
        return "Error solo letras de la A a la H"

        
letra=str(input("ingrese la letra de la columna: "))
numero=int(input("ingrese el numero de la fila: "))
print(ajedrez(letra,numero))