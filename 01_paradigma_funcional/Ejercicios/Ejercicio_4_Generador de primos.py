#Ejercicio: Generador de primos
#Implementar una función generadora que permita producir todos los números primos uno a uno.

#%%
def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()

for z in x:
  print(z)

#%%


def EsPrimo(n:int) -> bool:
  if n<2:
      return False
  else:
    for i in range(2,n):
       if n%i == 0:
          return False
  return True
       

def generadorPrimosHasta(end: int):
  ListaPrimos = []
  for n in range(end):
     if EsPrimo(n) == True:
      ListaPrimos.append(n)

  if len(ListaPrimos) == 0:
    return "No se encontraron primos"
  else:
    return ListaPrimos

if __name__ == "__main__":
  primos = generadorPrimosHasta(end=10)
  print(f"Los números primos en el rango son: {primos}")