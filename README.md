Ejercicios recursividad
Juan Camilo Espitia 20152020040
Angie Gabriela Antolinez 20151020061


def invertir(n,n):   
      if (n<10):  
         return n 
      else:        
          return n % 10+invertir(n / 10)* 10 

