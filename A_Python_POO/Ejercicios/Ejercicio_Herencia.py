#Consinga
"""
a) Crear una clase Vehiculo con los siguientes atributos y métodos:
● Atributos:
○ marca (String)
○ modelo (String)
○ precioBase (double).
● Métodos:
○ Un constructor que acepte la marca, modelo y precio base del vehículo.
○ Un método calcularCostoAlquiler(int dias) que calcule el costo de alquiler del vehículo
durante el número de días especificado. El costo se calcula como precioBase * dias.
b) Crear dos subclases Auto y Moto, que hereden de la clase Vehiculo. Las subclases deben incluir
un constructor que llame al constructor de la superclase y también deben sobrescribir el método
calcularCostoAlquiler(int dias) de la siguiente manera:
● Para Auto, el costo de alquiler se calcula incrementando un 20% el costo común.
● Para Moto, el costo de alquiler se calcula con un descuento del 15% respecto al vehículo"""


class Vehiculo():
    
    def __init__(self, marca: str, modelo: str, precioBase: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.precioBase = precioBase

    def calcularCostoAlquiler(self, dias: int) -> float:
        return self.precioBase * dias

    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio Base: {self.precioBase}"

#Subclases

class Auto(Vehiculo):

    def __init__(self, marca: str, modelo: str, precioBase: float) -> None:
        super().__init__(marca, modelo, precioBase)

    def calcularCostoAlquiler(self, dias: int) -> float:
        """Calcula el costo de alquiler del auto con un incremento del 20%."""
        costo_base = super().calcularCostoAlquiler(dias)
        return costo_base * 1.20

    def __str__(self) -> str:
        return f"Auto - {super().__str__()}"
    
class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precioBase: float) -> None:
        super().__init__(marca, modelo, precioBase)

    def calcularCostoAlquiler(self, dias: int) -> float:
        """Calcula el costo de alquiler de la moto con un descuento del 15%."""
        costo_base = super().calcularCostoAlquiler(dias)
        return costo_base * 0.85

    def __str__(self) -> str:
        return f"Moto - {super().__str__()}"
    
if __name__ == "__main__":
    #test by copi
    # Crear instancias de Vehiculo, Auto y Moto
    vehiculo = Vehiculo("Toyota", "Corolla", 100.0)
    auto = Auto("Ford", "Focus", 120.0)
    moto = Moto("Yamaha", "MT-07", 80.0)

    # Calcular costos de alquiler
    dias = 5
    print(f"Vehículo: {vehiculo}, Costo de alquiler por {dias} días: {vehiculo.calcularCostoAlquiler(dias)}")
    print(f"Auto: {auto}, Costo de alquiler por {dias} días: {auto.calcularCostoAlquiler(dias)}")
    print(f"Moto: {moto}, Costo de alquiler por {dias} días: {moto.calcularCostoAlquiler(dias)}")
