def producto(n,m):
    if m>1:
        return n+producto(n,m-1)
    return n
n=int(input("ingrese el numero 1: "))
m=int(input("ingrese el numero 2: "))
print("el resultado es ",producto(n,m))
