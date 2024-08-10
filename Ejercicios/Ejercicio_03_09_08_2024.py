#Ejercicio de orden superior
#%%
#Funciona ver _venv_
from typing import Callable

def wrapper(func: Callable[[], None])->None:
    f()
    print("Ejecutada f()")

def f():
    return True

wrapper(f)

#%%
#resuelto en clase

from collections.abc import Callable

def wrapper2(f: Callable[[], None]
    f2()
    print("Ejecutada f()")

def f2():
    pass