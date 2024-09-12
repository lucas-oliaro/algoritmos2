#Ejercicio: Modelar las zonas para censo

#Implementar las clases necesarias para modelar las diferentes zonas a censar,
#donde país es la más amplia y se compone de provincias, etc.

#Todas deben tener un atributo de subzonas que representa la lista de zonas que las conforman, 
#excepto la clase de vivienda que tiene el atributo habitantes.
#Finalmente, incorporar la operación recursiva de censar como método en la clase abstracta Zona

from abc import ABC,abstractmethod #para crear clases abs

#clase abstracta de zona
class Zona(ABC):
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.subZonas = []

    def agregarSubZona(self, subzona):
        self.subZonas.append(subzona)

    @abstractmethod
    def censar(self):
        pass


class Pais(Zona):
    def censar(self):
        total_habitantes = 0
        for subzona in self.subZonas:
            total_habitantes += subzona.censar()
        print(f"Total de habitantes en  {self.nombre}: {total_habitantes}")
            
        return total_habitantes

class Provincia(Zona):
    def censar(self):
        total_habitantes = 0
        for subzona in self.subZonas:
            total_habitantes += subzona.censar()
        print(f"Total de habitantes en {self.nombre}: {total_habitantes}")

        return total_habitantes

class Municipio(Zona):
    def censar(self):
        total_habitantes = 0
        for subzona in self.subZonas:
            total_habitantes += subzona.censar()
        
        print(f"Total de habitantes en {self.nombre}: {total_habitantes}")
        return total_habitantes

class Comuna(Zona):
    def censar(self):
        total_habitantes = 0
        for subzona in self.subZonas:
            total_habitantes += subzona.censar()
        print(f"Total de habitantes en {self.nombre}: {total_habitantes}")
        return total_habitantes

class vivienda(Zona):
    def __init__(self,Nombre:str , Habitantes: int) -> None:
        super().__init__(Nombre)
        self.habitantes = Habitantes

    def censar(self):
        print(f"Censando en: {self.nombre} con {self.habitantes} habitantes")
        return self.habitantes





vivienda1 = vivienda("Vivienda 1", 4)
vivienda2 = vivienda("Vivienda 2", 3)
vivienda3 = vivienda("Vivienda 3", 5)

# Crear barrios y agregar viviendas
barrio1 = Comuna("Barrio A")
barrio1.agregarSubZona(vivienda1)
barrio1.agregarSubZona(vivienda2)

barrio2 = Comuna("Barrio B")
barrio2.agregarSubZona(vivienda3)

# Crear municipio y agregar barrios
municipio = Municipio("Municipio 1")
municipio.agregarSubZona(barrio1)
municipio.agregarSubZona(barrio2)

# Crear provincia y agregar municipios
provincia = Provincia("Provincia 1")
provincia.agregarSubZona(municipio)

# Crear país y agregar provincias
pais = Pais("País X")
pais.agregarSubZona(provincia)

# Realizar el censo
pais.censar()