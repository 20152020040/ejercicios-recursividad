def longitud(n):
    if n<=10:
        return 1
    else:
        return int(1+longitud(n/10))
                   

def potencia(n,m):
    if m==0:
        return 1
    else:
        if m>1:
            return n*potencia(n,m-1)
        else:
            return n
                   
def invertir(n):
    if (n<10):
        return n
    else:
        return (n%10)*potencia(10,longitud(n)-1) + invertir(int(n/10))

def palindromo(n):
    if n<10:
        return "es palindromo";
    else:
        if n==invertir(n):
            return "es palindromo"
        else:
            return "no es palindromo"
    
n=int(input("ingrese el numero 1: "))
print("el resultado es ",palindromo(n))
