#multiplicaciones
def tablasMultiplicar(opcion):
    for i in range (1,11):
        if opcion==1:
            if(i%2==0):
                for i2 in range(1,11):
                    print(i, "*" ,i2, "=", (i2*i))
                print("\n")
        else:
            if(i%2!=0):
                for i2 in range(1,11):
                    print(i, "*" ,i2, "=", (i2*i))
                print("\n")

print("1.tabla de multiplicación (pares)")
print("2.tabla de multiplicación (impares)")
opcion=int(input("__"))

print(tablasMultiplicar(opcion))
