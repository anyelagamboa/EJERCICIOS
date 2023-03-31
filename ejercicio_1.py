#calculadora
def calculadora(numero1,signo,numero2):
    if(signo=="suma"):
        return (numero1 + numero2)
    elif (signo=="resta"):
        return (numero1-numero2)
    elif(signo=="multiplicacion"):
        return(numero1*numero2)
    elif(signo=="division" and numero2!=0):
        return (numero1/numero2)
    else:
        return "Error operación invalida"

numero1=int(input("Digite su primer numero: "))
signo=str(input("Digite la operacion que desea realizar (texto): "))
numero2=int(input("Digite su segundo numero: "))
print(calculadora(numero1,signo,numero2))