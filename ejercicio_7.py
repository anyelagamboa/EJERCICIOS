"""
58.Escriba un programa que lea una fecha del usuario y calcule su sucesor inmediato. 
Por ejemplo, si el usuario ingresa valores que representan 2013-11-18, 
su programa debería mostrar un mensaje que indica que el día inmediatamente 
posterior al 2013-11-18 es 2013-11-19. Si el usuario ingresa valores que representan 2013-11-30, 
el programa debe indicar que el día siguiente es 2013-12-01. Si el usuario ingresa valores 
que representan 2013-12-31, entonces el programa debe indicar que el día siguiente es 2014-01-01. 
La fecha se ingresará en forma numérica con tres declaraciones de entrada separadas; uno para el año, 
uno para el mes y otro para el día. Asegúrese de que su programa funcione correctamente durante los años bisiestos.
"""

def sigDia(año,mes,dia):
    if año>999 and año<10000: 
        if mes>0 and mes<13:
            if dia>0 and dia<32:
                if mes==2:
                    if dia==28:
                        return print(año,"/",mes+1,"/",1)
                    else:
                        return print(año,"/",mes,"/",dia+1)
                elif mes==12:
                    if dia==31:
                        return print(año+1,"/1","/1")
                    else:
                        return print(año,"/",mes,"/",dia+1)
                elif mes==4 or mes==6 or mes==9 or mes==11:
                    if dia==30:
                        return print(año,"/",mes+1,"/1")
                    else:
                        return print(año,"/",mes,"/",dia+1)
                else:
                    if dia==31:
                        return print(año,"/",mes+1,"/1")
                    else:
                        return print(año,"/",mes,"/",dia+1)
            else:
                return print("Error valor de dia solo de 01-31")
        else:
            return print("Error valor de mes solo de 01-12")
    else:
        return print("Error valor de año solo de 1000-9999")
    
año=int(input("Año: "))
mes=int(input("Mes: "))
dia=int(input("Dia: "))
print("___________")
sigDia(año,mes,dia)