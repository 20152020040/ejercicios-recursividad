# ejercicios-recursividad
1
def producto(n,m):
    if m>1:
        return n+producto(n,m-1)
    return n

2
def Cociente(n,m):
    if n<m:
        return 0
    else:
        return 1+cociente(n-m,m)

3
def potencia(n,m):
    if m==0:
        return 1
    else:
        if m>1:
            return n*potencia(n,m-1)
        else:
            return n
        

4
def fibo(n):
    if n==0:
        return 1
    else:
        if n==1:
            return 1
        else:
            if n>1:
                return fibo(n-1)+ fibo(n-2)

5
def sumaDig(n):
    if n<10:
        return n
    else:
       return int(sumaDig(n/10)+sumaDig(n%10))


6




7
def longitud(n):
    if n<=10:
        return 1
    else:
        return int(1+longitud(n/10))
