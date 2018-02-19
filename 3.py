def fibo(n):
    if n==0:
        return 1
    else:
        if n==1:
            return 1
        else:
            if n>1:
                return fibo(n-1)+ fibo(n-2)
    
n=int(input("ingrese el numero 1: "))
m=int(input("ingrese el numero 2: "))
print("el resultado es ",fibo(n))
