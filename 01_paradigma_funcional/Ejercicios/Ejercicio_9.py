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
