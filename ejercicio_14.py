"""
83.Un minorista en línea ofrece envío exprés para muchos de sus artículos a una tarifa de $10.95 
para el primer artículo y $2.95 para cada artículo subsiguiente. Escribe una función que tome 
el número de artículos en el pedido como su único parámetro. Devuelve los gastos de envío del 
pedido como resultado de la función. Incluya un programa principal que lea la cantidad de 
artículos comprados al usuario y muestre el cargo de envío.
"""

def CostoEnvio(cantidad_articulos):
    sum=10.95
    contador=1
    while contador < cantidad_articulos:
        sum+=2.95
        contador+=1
    return sum

cantidad_articulos=int(input("Cantidad de Articulos: "))

print("Costo del envio: ",CostoEnvio(cantidad_articulos))