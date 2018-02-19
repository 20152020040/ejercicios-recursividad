def longitud(n):
    if n<=10:
        return 1
    else:
        return int(1+longitud(n/10))
n=int(input("ingrese el numero 1: "))

print("el resultado es ",longitud(n))
