class Lamparita():

    def __init__(self) -> None:
        self.estado = False

    def prender(self):
        self.estado = True

    def apagar(self):
        self.estado = False

    def mostrar_estado(self):
       print("Apagado" if self.estado==False else "Prendido")
              
if __name__ == '__main__':
    lamparita = Lamparita()
    lamparita.mostrar_estado()
    lamparita.prender()
    lamparita.mostrar_estado()
    lamparita.apagar()
    lamparita.mostrar_estado()
    


