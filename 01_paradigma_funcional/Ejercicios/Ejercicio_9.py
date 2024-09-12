# Ejercicio: Conteo de elementos
# Definir utilizando reduce una operación que dada una lista de cadenas 
# devuelva un diccionario donde las claves sean cada elemento de la lista y 
# los valores sean la cantidad de apariciones que tiene ese elemento en la lista.

# Ejemplo: contar(['a', 'b', 'c', 'a', 'a', 'c', 'b', 'd', 'c', 'a', 'e']) -> {'a': 4, 'b': 2, 'c': 3, 'd': 1, 'e': 1}.

#%% 
# Idea personal
def contar(lista : list) -> dict:
    result = dict(zip(lista,map(lambda x: lista.count(x),lista)))
    #Uso de map en este caso: sobre x proveniente de lista aplica la funcion lista.count
    #zip solamente genera una tupla y dict convierte las tuplas en dict
    return result



if __name__ == "__main__":
    print(contar(['a', 'a', 'a'])) #-> {a : 3}
    print(contar(['a', 'b', 'c', 'a', 'a', 'c', 'b', 'd', 'c', 'a', 'e']))


# %%

#Solution GPT
from collections import Counter

def contar2(lista: list) -> dict:
    return dict(Counter(lista))

if __name__ == "__main__":
    print(contar2(['a', 'a', 'a'])) #-> {a : 3}
    print(contar2(['a', 'b', 'c', 'a', 'a', 'c', 'b', 'd', 'c', 'a', 'e']))


# %%
#Solution with reduce Personal

"""
The reduce(fun,seq) function is used to apply a particular function passed in its 
argument to all of the list elements mentioned in the sequence passed along.}
This function is defined in “functools” module.
"""
from functools import reduce

def contar3(lista: list) -> dict:
    return reduce(lambda acumulador, x: {**acumulador, x: acumulador.get(x, 0) + 1}, lista, {})
    # primero se genera el acumulador que es un dict vacio, luego se aplica la funcion lambda o sea x (en este caso).
    # el cual en la primera instacia agarra al dict vacio como key y value sera la busqueda de el iterable x con su valor + 1 (caso inicial no tiene o sea 0),
    # esto se realiza sobre el el dict (acumulador) 

# Ejemplo de uso
resultado = contar3(['a', 'b', 'c', 'a', 'a', 'c', 'b', 'd', 'c', 'a', 'e'])
print(resultado)
