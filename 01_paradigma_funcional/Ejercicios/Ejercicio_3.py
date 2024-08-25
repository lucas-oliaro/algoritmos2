#Proponer ejemplos de funciones impuras para cada tipo de efecto secundario mencionado y 
# cómo se podrían conventir, si es posible, a versiones de funciones puras.FF



#%%
#Modificación de Variables Globales: Una función impura puede modificar variables globales,
#alterando así el estado global del programa. Esto puede afectar a otras partes del código que dependen de esas variables.

contador1 = 0

def CambioNombre(nombre : str)->None:
    global contador1 
    frase = f'Hola {nombre}'
    contador1 +=1
    print(frase)

print(contador1)
CambioNombre("Pepe")
print(contador1)

#%%
#Solution
contador = 0

def CambioNombre2(nombre : str, contador : int)->tuple:
    frase = f'Hola {nombre}'
    nuevoContador = contador + 1 
    return frase, nuevoContador

print(contador)
frase, contador = CambioNombre2("Pepe",contador)
print(frase)
print(contador)


#%%
# Modificaci(ón de Argumentos: Una función impura puede modificar el valor asociado a un parámetro 
# (si se pasa por referencia) o alterar el estado de un objeto que se pase como argumento 
# (en lenguajes que aceptan el pasaje por valor de referencias). 
# Esto puede afectar a otras partes del código que dependen de esas variables.


miLista = ["A", "B", "C"]

def Impura2(Lista: list)-> list:
    """Modifica mi lista"""
    Lista.append("D")
    return Lista

def Pura2(Lista: list)-> list:
    #crea nueva lista 
    return Lista + ["D"]
#%%
#Operaciones de Entrada/Salida (I/O): Interacciones con el mundo exterior, 
# como lectura o escritura en archivos, envío de correos electrónicos, acceso a bases de datos, etc. 
# Estas operaciones son típicamente impuras ya que pueden tener efectos que van más allá de la propia ejecución de la función.


def impure_function():
    with open('data.txt', 'w') as f:
        f.write('Hello, World!')

def pure_function():
    return 'Hello, World!'

def write_to_file(data):
    with open('data.txt', 'w') as f:
        f.write(data)



#%%
#Impresiones en Consola o Registro de Eventos: La impresión en la consola o el registro de eventos (logging) también se considera un efecto secundario, ya que implica una interacción con el entorno fuera de la función, son operaciones de salida.

def Impura3(x):
    print(f"El valor es: {x}")
    return x * 2

def Pura3(x):
    return x * 2

def log_value(x):
    print(f"El valor es: {x}")

#%%
#-Interacciones de Red: Las operaciones de red, como solicitudes a una API, también pueden ser impuras, ya que están interactuando con el entorno.

import requests

def Impura4(url):
    response = requests.get(url)
    return response.json()

def Pura4(data):
    # Proceso de los datos recibidos
    return len(data)

def fetch_data(url):
    response = requests.get(url)
    return response.json()



#%%
#-Llamadas a Funciones con Efectos Secundarios: Si una función llama a otra función impura, automáticamente se convierte en una función impura también. A su vez, si ambas producen efectos colaterales, se pueden acumular y propagarse.


def another_impure_function():
    print("Doing something...")

def Impura5(x):
    another_impure_function()
    return x * 2

#Solution
def Pura5(x):
    return x * 2

#%%
#Generación de Números Aleatorios: Si una función genera números aleatorios, su resultado puede variar en diferentes llamadas, lo que introduce una variabilidad no determinista.

import random

def Impura6():
    return random.randint(1, 10)

#Semilla fija como se comparta
def Pura6(seed):
    random.seed(seed)
    return random.randint(1, 10)

