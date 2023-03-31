"""
78.Escriba un programa que convierta un número decimal (base 10) a binario (base 2). 
Lea el número decimal del usuario como un número entero y luego use el algoritmo de división 
que se muestra a continuación para realizar la conversión. Cuando se completa el algoritmo, 
el resultado contiene la representación binaria del número. Muestre el resultado, junto con un mensaje apropiado.
Deje que el resultado sea una cadena vacía
Sea q el número a convertir
repetir
Establecer r igual al resto cuando q se divide por 2
Convierta r en una cadena y agréguela al comienzo del resultado
Divida q por 2, descartando cualquier resto, y almacene el resultado nuevamente en q
hasta que q sea 0
"""
def DecimalABinario(numero):
    rta=0
    contador=0
    while numero!=0 :
        residuo=numero%2
        numero=numero//2
        rta=rta+(residuo*(10**contador))
        contador+=1
    return rta

numero=int(input("Ingrese un número (Dec a Bin): "))
print("El número ",numero," en Binario es ",DecimalABinario(numero))