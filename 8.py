def mayorDig(n):
    if (n<10):
        return n
    else:
        if (mayorDig(n%10)*10>mayorDig(n/10)*10):
            return int(mayorDig(n%10))
        else:
            return int(mayorDig(n/10))
n=int(input("ingrese el numero 1: "))

print("el resultado es ",mayorDig(n))
