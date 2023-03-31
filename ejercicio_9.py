"""
67.Un zoológico en particular determina el precio de la entrada según la edad del visitante. 
Los huéspedes de 2 años de edad y menos se admiten sin cargo. Niños entre 3 y 12 años cuestan $14.00. 
Las personas mayores de 65 años o más cuestan $ 18.00. La entrada para todos los demás invitados es de $23.00. 
Cree un programa que comience leyendo las edades de todos los invitados en un grupo del usuario, 
con una edad ingresada en cada línea. El usuario ingresará una línea en blanco para indicar que no hay más invitados 
en el grupo. Luego, su programa debe mostrar el costo de admisión para el grupo con un mensaje apropiado. 
El costo debe mostrarse con dos decimales.
"""

def zoologico():
    print("PRECIOS \n"
          "0-2 años = 0 \n"
          "3-12 años = 14.00 \n"
          "13-64 años = 23.00 \n"
          "65 o mas años = 18.00 \n")
    edad=int(input("Ingrese la edad: "))
    total=0
    contador = 1
    while edad >-1:
        if edad>-1 and edad<3:
            total+=0
        elif edad>2 and edad<13:
            total+=14.00
        elif edad>12 and edad<65:
            total+=23.00
        else:
            total+=18.00
        contador+=1
        edad=int(input("Ingrese la edad: "))
    print("En total fueron ",contador-1," entradas con un costo total de ",total) 

zoologico()

    