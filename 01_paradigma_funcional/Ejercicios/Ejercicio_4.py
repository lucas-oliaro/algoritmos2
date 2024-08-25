#Ejercicio: Generador de primos
#Implementar una función generadora que permita producir todos los números primos uno a uno.
def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()

for z in x:
  print(z)



def generadorPrimosHasta(end: int):
  
    for _ in range(end):
       print
    

if __name__ ==  "__main__":
  generadorPrimosHasta(end=10)