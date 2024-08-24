"""Implemente la clase Punto (pares de coordenadas de tipo float x, y). Defina
constructores y métodos para asignar valores a las coordenadas de los puntos,
retornar el valor de cada coordenada, y sumar dos puntos, retornando su
resultado. Definir un método booleano de igualdad entre dos puntos"""

class Punto():

    def __init__(self,x=0.0 ,y= 0.0) -> None:
        self.x = x
        self.y = y 


    def SetX(self,x_value: float):
        self.x = x_value

    def SetY(self, y_value: float):
        self.y = y_value

    def Get_X_Value(self)->float:
        return self.x
    
    def Get_Y_Value(self)->float:
        return self.y
    
    def Suma(self, otroPunto):
        if isinstance(otroPunto, Punto):
            return Punto(x = self.Get_X_Value() + otroPunto.Get_X_Value(),
                        y = self.Get_Y_Value() + otroPunto.Get_Y_Value())
        else:
            raise ValueError("Debe ser un Punto")
        
    def __eq__(self, otroPunto: object) -> bool:
        return isinstance(otroPunto, Punto) and self.Get_X_Value() == otroPunto.Get_X_Value() and self.Get_Y_Value() == otroPunto.Get_Y_Value()

    def __repr__(self) -> str: #Representacion del punto para uso "interno"
        return f'Punto (x= {self.Get_X_Value()},y= {self.Get_Y_Value()}  )'        
    
    def __str__(self) -> str: #Lectura usuario
        return f"El punto es (x={self.Get_X_Value()}, y={self.Get_Y_Value()})"

#Evaluacion del codigo by Copi

# Crear un punto con coordenadas predeterminadas
p1 = Punto()
print(p1)  # Output: El punto es (x=0.0, y=0.0)

# Crear un punto con coordenadas específicas
p2 = Punto(3.5, 4.5)
print(p2.Get_X_Value())  # Output: 3.5
print(p2.Get_Y_Value())  # Output: 4.5

# Modificar las coordenadas del punto
p2.SetX(5.0)
p2.SetY(6.0)
print(p2)  # Output: El punto es (x=5.0, y=6.0)

# Crear dos puntos
p3 = Punto(1.0, 2.0)
p4 = Punto(3.0, 4.0)

# Sumar los puntos
p5 = p3.Suma(p4)
print(p5)  # Output: El punto es (x=4.0, y=6.0)


# Crear puntos
p6 = Punto(2.0, 3.0)
p7 = Punto(2.0, 3.0)
p8 = Punto(4.0, 5.0)

# Comparar puntos
print(p6 == p7)  # Output: True (mismo valor)
print(p6 == p8)  # Output: False (diferentes valores)
