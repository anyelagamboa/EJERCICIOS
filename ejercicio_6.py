"""
51.En una universidad en particular, las calificaciones con letras 
se asignan a puntos de calificación de la siguiente manera:

Escriba un programa que comience leyendo una letra de calificación del usuario. 
Luego, su programa debería calcular y mostrar el número equivalente de puntos de calificación. 
Asegúrese de que su programa genere un mensaje de error apropiado si el usuario 
ingresa una calificación de letra ´++ inválida.

"""

def calificacion(nota):
    if nota=="A+" or nota=="A":
        return "Su calificación es de 4.0 "  
    elif nota=="A-":
        return "Su calificación es de 3.7 "    
    elif nota=="B+":
        return "Su calificación es de 3.3 "
    elif nota=="B":
        return "Su calificación es de 3.0 "
    elif nota=="B-":
        return "Su calificación es de 2.7 "
    elif nota=="C+":
        return "Su calificación es de 2.3 "
    elif nota=="C":
        return "Su calificación es de 2.0 "
    elif nota=="C-":
        return "Su calificación es de 1.7 "
    elif nota=="D+":
        return "Su calificación es de 1.3 "
    elif nota=="F":
        return "Su calificación es de 0.0 "
    else:
        return"Error valor invalido (letras en mayuscula)"
    

nota=str(input("Ingrese la calificación : "))
print(calificacion(nota))