#Ejercicio: Pipeline de datos con generadores
#un lector de archivo CSV utilizando 3 generadores:
#    uno para producir cada línea leída del archivo.
#    otro para producir una lista de campos string a partir de cada línea leída, consumiendo el generador previo.
#    otro para producir un diccionario a partir de cada lista de campos obtenida con el generador previo.
#calcular la suma de los sepal_width de todas las especies Iris-setosa del dataset IRIS.csv, utilizando un generador que produzca cada valor de sepal_width de una planta a la vez que sea de esa especie. Valor esperado: 170.9
#similar al punto anterior, pero calculando el promedio del sepal_width de las especies Iris-setosa. Valor esperado: 3.418

