# Intro Arboles

Se utiliza arboles cuando se quiere representar una realaicon jerarquica
> "“El árbol es una estructura que permite representar un orden jerárquico de una colección de elementos"

[![App Platorm](https://github.com/lucas-oliaro/algoritmos2/raw/main/03_arboles/imagenes/organigrama.png)](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/intro_arboles.md)

Otros casos de uso son:
- Representar flujos de procesos de decisión
- Optimizar la búsqueda sobre estructuras lineales
- Representar estructuras jerárquicas como taxonomías o clasificaciones

Caracteristica del arbol
>es una estructura que permite representar un orden jerárquico de una colección de elementos.


Un caso de uso de particular interes para nuestro campo:
Un arbol de decision que se utiliza ocmo modelo predictivo de machine learning. Cada nodo representa una pregunta que tiene respuesta un conjunto de respeuestas posibles y en cada subarbol se concentran las observaciones que cumplan con las ocndiciones de las respuestas acorde a cada pregunta. Por ejemplo, la hoja con etiqueta

[//]: <> (How to put images.)
[![App Platorm](https://github.com/lucas-oliaro/algoritmos2/raw/main/03_arboles/imagenes/arbol_decision.png)](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/intro_arboles.md)


## Definciones

Un **arbol `T`** es un conjunto finito de cero o más nodos `(v1, v2, …, vn)` donde:
- un nodo especial llamado  **raíz**
- los nodos se particionan en `m` conjuntos _disjuntos_ `T1, T2, …, Tm`, donde cada uno es un arbol con el nodo **raiz** como _ancestro directo_
- compuesto por _nodos_ o _vertices_
- compuest por _arcos_ o _aristas_

_Ejemplo_
[![App Platorm](https://github.com/lucas-oliaro/algoritmos2/raw/main/03_arboles/imagenes/arbol_definiciones.png)](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/intro_arboles.md)


En una relación de orden jerárquico se podría decir que el nodo 1 es predecesor de todos, mientras que el nodo 3 es predecesor del 6. Los nodos 2 y 3 son descendientes directos del nodo 1.
> Una rama es una secuencia de nodos conectados que comienza con el nodo raíz y finaliza en una hoja.

Un **bosque** es un conjunto de **`T1, T2, …, Tm`

## Implementación

### *con recursion directa*
si estuviésemos modelando un mapa de contagios de un virus, donde cada nodo representa un paciente y los descendientes directos a las personas que contagió, probablemente la _etiqueta_ para identificar cada nodo sería un número de historia clínica del paciente.

> La **etiqueta de un nodo** debería poder representar a cada nodo de forma simple y única para luego facilitar operaciones de búsqueda, edición y eliminación dentro de la estructura.

```python
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class ArbolBinario(Generic[T]):
    def __init__(
        self, 
        dato: T, 
        si: Optional[ArbolBinario[T]] = None, 
        sd: Optional[ArbolBinario[T]] = None
    ):
        self.dato: T = dato
        self.si: Optional[ArbolBinario[T]] = si
        self.sd: Optional[ArbolBinario[T]] = sd

```

Esta estrategia de implementación utiliza una estructura con recursión directa, donde se establece el dato genérico de tipo `T` que almacena la información del nodo y los subárboles izquierdo y derecho en los atributos ``si`` y ``sd``, respectivamente. La representación de una hoja se logra determinando en None a los subárboles.

> Si bien es suficiente para definir un árbol binario, sucede que es complicada para representar la abstracción de un árbol vacío

### con recursion mutua
Una estructura alternativa sería utilizando dos abstracciones, una para los nodos y otra para el árbol en sí. De esa forma es más sencillo modelar la abstracción de árbol vacío ya que permite _anular_ la raíz de un árbol con ``None``.


```python
from typing import Generic, Optional, TypeVar

T = TypeVar('T')
class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None

    def es_vacio(self) -> bool:
        return self.raiz is None

class NodoAB(Generic[T]):
    def __init__(
        self, 
        dato: T, 
        si: Optional[ArbolBinario[T]] = None, 
        sd: Optional[ArbolBinario[T]] = None
    ):
        self.dato: T = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

# Initialize the tree
tree = ArbolBinario[int]()

# Add a root node with value 10
tree.raiz = NodoAB(10)

# Add left child with value 5 and right child with value 15
tree.raiz.si = NodoAB(5)
tree.raiz.sd = NodoAB(15)
```
La clase genérica `ArbolBinario` ahora tiene un constructor que sólo permite instanciar **árboles vacíos**, que se representan con un único atributo `raiz` asignado a `None`. Si necesitamos construir un nodo del árbol, recurrimos a otra clase `NodoAB` que contiene tanto el dato del nodo en su atributo `dato` y los subárboles descendientes en sus atributos `si` y `sd`. Luego, el objeto de tipo `NodoAB` es asignado al atributo `raiz` de un objeto `ArbolBinario`.


> to understand more please use https://pythontutor.com/render.html#mode=display 

Si deseamos encapsular y ocultar la clase NodoAB evitando exponerla en el módulo, para generar un árbol no vacío, podríamos definir un método constructor estático así:
```python
@staticmethod
def crear_nodo(
    dato: T, 
    si: Optional[ArbolBinario[T]] = None, 
    sd: Optional[ArbolBinario[T]] = None
) -> ArbolBinario[T]:
    t = ArbolBinario()
    t.raiz = NodoAB(dato, si, sd)
    return t

#Caso de uso
# Crear subárboles izquierdo y derecho
izquierdo = ArbolBinario.crear_nodo(5)
derecho = ArbolBinario.crear_nodo(15)

# Crear el árbol principal con raíz 10 y los subárboles izquierdo y derecho
arbol_principal = ArbolBinario.crear_nodo(10, izquierdo, derecho)

```

## Operaciones AKA Atributos
Implementaciones de nuevas operaciones a nuestra estrucutra con elementos.

### Vincular un ancestro directo
Agregar una referencia al nodo antecesor inmediato para facilitar la busqueda o recorrido inverso del arbol a partir de un nodo no raíz.


[![App Platorm](https://github.com/lucas-oliaro/algoritmos2/raw/main/03_arboles/imagenes/arbol_binario_antecesor.png
)](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/intro_arboles.md)

>tiene como desventaja el mantenimiento adicional necesario al momento de modificar el árbol, donde se debe no sólo reemplazar referencias a subárboles sino también al nodo predecesor.


```python
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class NodoAB(Generic[T]):
    def __init__(
        self, 
        dato: T, 
        si: Optional[ArbolBinario[T]] = None, 
        sd: Optional[ArbolBinario[T]] = None
    ):
        self.dato: T = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

class ArbolBinario(Generic[T]):     
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None
        self.antecesor: Optional[ArbolBinario[T]] = None

    def es_vacio(self) -> bool:
        return self.raiz is None


    @staticmethod
    def crear_nodo(
        dato: T, 
        si: Optional[ArbolBinario[T]] = None, 
        sd: Optional[ArbolBinario[T]] = None
    ) -> ArbolBinario[T]: 
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        t.raiz.si.antecesor = t
        t.raiz.sd.antecesor = t

        return t

    def insertar_si(self, si: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio')
        self.raiz.si = si
        self.raiz.si.antecesor = self
```


### Operaciones básicas
Veamos algunas de las operaciones absicas que podemos integrar en nuestra implementacion de arbol binario.

Estas **operaciones proyectoras** nos permiten conocer aspectos básicos de la estructura. si y sd devuelven los subárboles izquierdo y derecho, respectivamente. dato nos entrega la información almacenada en la raíz de ese árbol. es_hoja nos indica si el árbol actual es una hoja, es decir, cuando no se trate de un árbol vacío y no tiene subárboles descendientes.


```python
def si(self) -> "ArbolBinario[T]":
    if self.es_vacio():
        raise TypeError('Arbol Vacio') 
    return self.raiz.si

def sd(self) -> "ArbolBinario[T]":
    if self.es_vacio():
        raise TypeError('Arbol Vacio') 
    return self.raiz.sd

def dato(self) -> T:
    if self.es_vacio():
        raise TypeError('Arbol Vacio') 
    return self.raiz.dato

def es_hoja(self) -> bool:
    return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

```

Estas **operaciones modificadoras** se ocupan de alterar la estructura actual incorporando o reemplazando nuevos subárboles a la raíz del árbol actual.

```python
def altura(self) -> int:
    if self.es_vacio():
        return 0
    else:
        return 1 + max(self.si().altura(), self.sd().altura())
    
def __len__(self) -> int:
    if self.es_vacio():
        return 0
    else:
        return 1 + len(self.si()) + len(self.sd())

```


**Otras operaciones**: Similar al cálculo de la longitud de una lista, donde la misma se computa sumando 1 a la longitud de su cola, la altura de un árbol se calcula con el máximo de las alturas de sus subárboles incrementado en 1 (el nodo actual). El caso base se define para el árbol vacío donde resulta con altura 0.
```python
def altura(self) -> int:
    if self.es_vacio():
        return 0
    else:
        return 1 + max(self.si().altura(), self.sd().altura())
    
def __len__(self) -> int:
    if self.es_vacio():
        return 0
    else:
        return 1 + len(self.si()) + len(self.sd())
```


## Summary
Se completa la introduccion a Arboles.

**Definición de Árboles**

- Estructura para representar relaciones jerárquicas.
- Consta de nodos y arcos, con un nodo especial llamado raíz.
- Se puede considerar un árbol como un conjunto de nodos divididos en subgrupos disjuntos.

**Casos de uso**

- Representación de flujos de procesos de decisión.
- Optimización de búsquedas en estructuras lineales.
- Representación de taxonomías y clasificaciones.

**Características de un Árbol**

- Cada árbol tiene una raíz y nodos que pueden tener descendientes.
- Un bosque es un conjunto de árboles.

**Implementación**

- Con **_Recursión Directa_**: Utiliza un único nodo que contiene el dato y referencias a subárboles izquierdo y derecho.
- Con **_Recursión Mutua_**: Separa la estructura de nodo y árbol, permitiendo representar árboles vacíos más fácilmente.

**Operaciones Básicas**

- Métodos para acceder a subárboles (izquierdo y derecho) y obtener datos del nodo raíz.
- Métodos para verificar si un árbol es hoja y calcular su altura y longitud.

**Operaciones Modificadoras**
- Métodos para insertar nuevos subárboles y modificar la estructura del árbol.

### Ejercicios Propuestos

`Arbol_Binario`
**ejercicoo 1**
Dentro del TAD ArbolBinario una función recursiva nivel, que dado un valor, retorne en qué nivel se encuentra en el nodo del árbol. Si el valor no se encontrara en el árbol, retornar un valor superior a la altura del árbol.

#### Resolucion 

Mucha recursion (_esta complicada la cosa_)

```python
def nivel(self, x: T) -> int:
        if self.es_vacio():
            return 0  
        elif self.dato() == x:
            return 1  
        else:
            nivel_izq = self.si().nivel(x) if not self.si().es_vacio() else 0
            nivel_der = self.sd().nivel(x) if not self.sd().es_vacio() else 0

        return 1 + min(nivel_izq, nivel_der) 
```

**Ejercicio 2**
Desarrollar dentro del TAD ArbolBinario una función recursiva copy, que devuelva la deep copy
de un árbol (el prototipo se encuentra en el template)

```python
def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            new_t = ArbolBinario.crear_nodo(self.dato())

            # inserto sub arboles
            new_t.insertar_si(self.si().copy())
            new_t.insertar_sd(self.sd().copy())
            return new_t
```


## Estrategias de Recorridos
Tenemos 3 estrategias para recorrer el arbol con la estrategia **_Primero en profundidad - DFS_**

### Primero en profundiadd - DFS
El objetivo de esta forma de recorrer un árbol es p_riorizar el recorrido de un subárbol_ antes de avanzar con el siguiente. 
Lo importante es recordar que el recorrido DFS (**Depth First Search**) siempre se recorre un subárbol completo antes de recorrer el o los restantes.

>Los algoritmos de recorrido en profundidad utilizan recursión múltiple y se apoyan en la pila de ejecución.

Podemos diferenciar los recorridos en profundidad en tres variantes que vemos a continuación. La operación de visita representa una abstracción que puede ser cualquier comportamiento sobre un nodo, sea mostrarlo, insertarlo en una lista, etc.


#### PreOrder R-I-D
En un recorrido **DFS preorder** primero se visita el nodo raíz, luego se visita en el mismo orden los nodos del subárbol izquierdo y a continuación se visita en el mismo orden los nodos del subárbol derecho.

[![App Platorm](https://github.com/lucas-oliaro/algoritmos2/raw/main/03_arboles/imagenes/dfs_preorder.png)](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/intro_arboles.md)

##### Implementacion
```python
def preorder(self):
    if not self.es_vacio():
        visita(self.dato())
        self.si().preorder()
        self.sd().preorder()
```

#### Inorder I-R-D
En un recorrido DFS inorder primero se visita en el mismo orden los nodos del subárbol izquierdo, luego el nodo raíz y finalmente se visita en el mismo orden los nodos del subárbol derecho.

[![App Platorm](https://github.com/lucas-oliaro/algoritmos2/raw/main/03_arboles/imagenes/dfs_inorder.png)](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/intro_arboles.md)

##### Implementacion
```python
def inorder(self):
    if not self.es_vacio():
        self.si().inorder()
        visita(self.dato())
        self.sd().inorder()
```

#### Postorder I-D-R
En un recorrido DFS postorder primero se visita en el mismo orden los nodos del subárbol izquierdo, luego se visita en el mismo orden los nodos del subárbol derecho, y finalmente se visita al nodo raíz.

[![App Platorm](https://github.com/lucas-oliaro/algoritmos2/raw/main/03_arboles/imagenes/dfs_postorder.png)](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/intro_arboles.md)

##### Implementacion
```python
def postorder(self):
    if not self.es_vacio():
        self.si().postorder()
        self.sd().postorder()
        visita(self.dato())
```

### Primero a lo ancho - BFS (R->I-D)
La estrategia de recorrido a lo ancho o **BFS** (Breadth First Search) es completamente diferente a las anteriores, ya que se recorren los nodos de un árbol por niveles. El primer nodo a recorrer es el nodo raíz y luego continúan los nodos del siguiente nivel, sus descendientes directos, y así sucesivamente. El orden de recorrido de cada nivel es arbitrario y suele hacerse de izquierda a derecha.
>Dado que el recorrido BFS utiliza una cola explícita, su implementación resulta en una recursión lineal de cola, la cual puede reemplazarse sencillamente en una iteración.

[![App Platorm](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/imagenes/bfs.png)](https://github.com/lucas-oliaro/algoritmos2/blob/main/03_arboles/intro_arboles.md)

**Ventaja**
si estuviéramos buscando un nodo que cumpla cierto requisito dentro de un árbol, la búsqueda a lo ancho garantiza que se encontrará (si existiera) el nodo correspondiente más cercano a la raíz.

#### Implementacion
```python
def bfs(self):
    def recorrer(q: list[ArbolBinario[T]]):
        if q:
            actual = q.pop()                # desencolar árbol visitado
            if not actual.es_vacio():
                visitar(actual.dato())
                q.insert(0, actual.si())    # encolar subárbol izquierdo
                q.insert(0, actual.sd())    # encolar subárbol derecho
            recorrer(q, recorrido)
            
    q: list[ArbolBinario[T]] = []
    q.insert(0, self)                       # encolar raíz
    recorrer(q)
```
Esta versión inicializa una cola (queue) que contiene al árbol a recorrer (el nodo raíz) y luego invoca la operación interna recorrido pasando como argumento a la cola. La idea es desencolar para obtener un nodo a visitar y luego encolar los subárboles del mismo en la cola. Esto se realiza repetidas veces hasta que no queden nodos en la cola.

Es importante notar que eventualmente la recursión termina (llega al caso base de una cola vacía) porque en todas las instancias recursivas se desencola un nodo, pero no necesariamente siempre se enconlan los descendientes. Las inclusiones de subárboles en la cola están condicionadas a si estamos ante un árbol no vacío.

### Ejercicios propuestos

#### Ejercicio: Generar listas de recorridos
Adaptar los diversos recorridos de árbol binario propuestos de forma que la operación de visita sea la de incoporar el dato del nodo en una lista, lo cual nos permita reflejar el orden del recorrido en una estructura lineal `list[T]`.

#### Ejercicio: Recorrido bottom-up
Implementar un algoritmo que devuelva el recorrido de un árbol desde las hojas hasta la raíz, y de izquierda a derecha. El primer nodo del recorrido debería ser la hoja más profunda y a la derecha, y último nodo debería ser el nodo raíz.

#### Ejercicio: Eliminar recursión en DFS
Implementar una versión de recorrido DFS inorder con recursión de cola.


# Árbol N-Ario
