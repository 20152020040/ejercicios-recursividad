def invertir(n):   
      if (n<10):  
         return n 
      else:        
          return (n%10)*potencia(10,longitud(n)-1) +invertir(int(n / 10))

def potencia(n,m):
    if m==0:
        return 1
    else:
        if m>1:
            return n*potencia(n,m-1)
        else:
            return n

def longitud(x):
    if x<=10:
        return 1
    else:
        return int(1+longitud(x/10))


n=int(input("ingrese el numero 1: "))

print("el resultado es ", invertir(n))
