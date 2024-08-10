#Ejercicio: Función de orden superior
#%%

"""1)Implementar una función llamada wrapper que reciba por parámetro a otra función f sin
argumentos, la ejecute e imprima en pantalla el mensaje de ejecución: "Ejecutada f()"."""

from collections.abc import Callable

def wrapper(f: Callable[[], None])->None:
    f()
    print("Ejecutada f()")

def f():
    pass

wrapper(f)

#%%

"""2)Extender la función wrapper de forma que pueda aceptar cualquier función con
argumentos variables y se puedan pasar también desde la función wrapper para que se
invoquen en f. Por ejemplo, si f acepta 3 argumentos, éstos deberían también pasarse a
wrapper para que se invoque f(arg1, arg2, arg3) dentro."""

from collections.abc import Callable

def wrapper2(f: Callable[..., None], *args, **kwargs)->None: # *args as tuple, **kwargs as dict
    f(*args, **kwargs)
    print("Ejecutada f()")


def f2(*args, **kwargs):
    for e in args:
        print(e)
    for k, v in kwargs.items():
        print(k, v)

wrapper2(f2, 1, 2, 3, a=4, b=5)
wrapper2(f2)
    



# %%
