def potencia(n,m):
    if m==0:
        return 1
    else:
        if m>1:
            return n*potencia(n,m-1)
        else:
            return n
    
n=int(input("ingrese el numero 1: "))
m=int(input("ingrese el numero 2: "))
print("el resultado es ",potencia(n,m))
