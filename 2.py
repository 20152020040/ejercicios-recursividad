def Cociente(n,m):
    if n<m:
        return 0
    else:
        return 1+Cociente(n-m,m)
    
n=int(input("ingrese el numero 1: "))
m=int(input("ingrese el numero 2: "))
print("el resultado es ",Cociente(n,m))
