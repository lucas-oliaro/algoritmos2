#Ejercicio de orden superior
#%%
#Funciona ver _venv_
from typing import Callable

def wrapper(func: Callable[[], None])->None:
    f()
    print("Ejecutada f() en 1")

def f():
    return True

wrapper(f)

#%%
#resuelto en clase

from collections.abc import Callable

def wrapper2(f: Callable[[], None])->None:
    f2()
    print("Ejecutada f() en 2")

def f2():
    pass

wrapper2(f2)
# %%
