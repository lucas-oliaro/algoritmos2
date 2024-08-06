class Restaurant():
    cant_sucursales = 0
    salario_promedio = 2000

    def __init__(self,nombre, ciudad, ubicacion, cantEmpleados: int):
        self.nombre = nombre
        self.ciudad = ciudad
        self.ubicacion = ubicacion
        self.cantEmpleados = cantEmpleados
        Restaurant.cant_sucurusales =+ 1

    @classmethod
    def obtenerNumerosSurcusales(cls):
        cls.cant_sucursales

    def obtener_salario_promedio(self):
        return self.salario_promedio

    def obtener_cant_empleados(self):
        return self.cantEmpleados

    def calcular_costo_operativo(self):
        return self.obtener_cant_empleados() * Restaurant.salario_promedio
    

if __name__ == "__main__":
    Resto_1 = Restaurant("R1", "Baires", "-38.05 -35.055", 5)
    Resto_2 = Restaurant("R2", "Cordoba", "-38.05 -35.055", 15)
    Resto_3 = Restaurant("R3", "Baires", "-38.05 -35.055", 15)
