"""
63.Escriba un programa que muestre una tabla de conversión de temperatura para grados Celsius 
y grados Fahrenheit. La tabla debe incluir filas para todas las temperaturas entre 0 y 100 grados 
Celsius que sean múltiplos de 10 grados Celsius. Incluya títulos apropiados en sus columnas. 
La fórmula para convertir entre grados Celsius y grados Fahrenheit es °F=(1.8*°C)+32.
"""

def CentigradosAFahrenheit():
    print("CENTIGRADOS / FAHRENHEIT")
    for centigrados in range (0,101,10):
        fahrenheit=(1.8*centigrados)+32
        print(centigrados,"C° = ",fahrenheit,"F°")

CentigradosAFahrenheit()
