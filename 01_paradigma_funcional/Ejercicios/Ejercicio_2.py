#Implementar una versión de un conjunto de elementos de cualquier tipo que
#sea inmutable. Podemos apoyarnos en la tuple de Python. El conjunto se
#crea con una cantidad de elementos variables y luego ya no puede
#modificarse.


#%%
from typing import Any

class MiClaseInmutable1:
    __slots__ = ('_elements',) #solo se permite el atributo _elements
    '''
    Define un conjunto fijo de atributos que un objeto puede tener,
    en este caso, solo _elements. Esto elimina la necesidad de un 
    diccionario interno (__dict__) para almacenar los atributos, 
    lo que reduce el consumo de memoria y hace que la clase sea más estricta.
    '''
    
    def __init__(self, *elements):
        super().__setattr__('_elements', tuple(set(elements)))

    def __setattr__(self, __name: str, value: Any) -> None:
        raise AttributeError(f'No es posible setear el atributo {__name}')
    """
    Este método se llama cada vez que se intenta asignar un valor a un
    atributo de la instancia, como mi_objeto.algo = valor.
    """

    def __delattr__(self, __name: str) -> None:
        raise AttributeError(f'No es posible eliminar el atributo {__name}')

    def valor(self):
        return self._elements
    
    
mi_objeto = MiClaseInmutable1(1, 2, 3, 4,4,5)
print(mi_objeto.valor())  # (1, 2, 3, 4)

# Intentar modificar el objeto lanzará una excepción
try:
    mi_objeto.nuevo_atributo = 9
except AttributeError as e:
    print(e)  # No es posible setear el atributo nuevo_atributo

# %%
