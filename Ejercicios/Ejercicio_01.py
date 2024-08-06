class Lampara():

    def __init__(self) -> None:
        self.estado = False

    def prender(self):
        self.estado = True

    def apagar(self):
        self.estado = False

    def mostrar_estado(self):
       print("Apagado" if self.estado==False else "Prendido")
              
    #@classmethod
    #def seCortoLaLuz(cls):
        #Ver


if __name__ == '__main__':
    print("Lampara ")
    lamparita = Lampara()
    lamparita.mostrar_estado()
    lamparita.prender()
    lamparita.mostrar_estado()
    lamparita.apagar()
    lamparita.mostrar_estado()
    print("Lampara 2")
    
    lamparita1 = Lampara()
    lamparita1.mostrar_estado()
    lamparita1.prender()
    lamparita1.mostrar_estado()


    print("Se apagan ambas")
    #Lampara.seCortoLaLuz()
    #lamparita.mostrar_estado()
    #lamparita1.mostrar_estado()


