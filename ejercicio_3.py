"""
36.En este ejercicio, creará un programa que lea una letra del alfabeto del usuario. 
Si el usuario ingresa a, e, i, o o u entonces su programa debería mostrar 
un mensaje que indica que la letra ingresada es una vocal. Si el usuario ingresa y,
su programa debería mostrar un mensaje que indica que a veces y es una vocal
y otras veces es una consonante. De lo contrario, su programa debería mostrar 
un mensaje que indique que la letra es una consonante.
"""

def consonanteOvocal(letra):
    if (letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or \
        letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U") :
        return "VOCAL"
    elif letra=="y" or letra=="Y":
        return "VOCAL O CONSONANTE"
    else:
        return "CONSONANTE"
    
letra=str(input("Ingrese una letra: "))
print ("La letra ", letra, " es una ",consonanteOvocal(letra) )