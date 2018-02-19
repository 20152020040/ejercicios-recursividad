def sumaDig(n):
    if n<10:
        return n
    else:
        return int(sumaDig(n/10)+sumaDig(n%10))
    
n=int(input("ingrese el numero 1: "))

print("el resultado es ",sumaDig(n))
