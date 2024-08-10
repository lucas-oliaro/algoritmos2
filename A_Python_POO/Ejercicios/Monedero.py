#Implemente una clase Monedero que permita gestionar la cantidad de dinero que
#una persona dispone en un momento dado. La clase deberá tener un constructor
#que permitirá crear un monedero con una cantidad de dinero inicial y deberá
#definir un método para meter dinero en el monedero, otro para sacarlo y
#finalmente, otro para consultar el disponible; solo podrá conocerse la cantidad de
#dinero del monedero a través de este último método. Por supuesto, no se podrá
#sacar más dinero del que haya en un momento dado en el monedero.

class Monedero:
    def __init__(self, dinero: float):
        self.dinero= dinero

    def IngresoDinero(self,amount: float):
        self.dinero = self.dinero + amount
        print(f"Dinero ingresado: {amount},  {self.ConsultarSaldo()}")

    def RetirarDinero(self, amount: float):
        if self.dinero> amount:
            self.dinero = self.dinero - amount
            print(f"Dinero retirado: {amount}. {self.ConsultarSaldo()}")
        else:
            print("no se puede extraer más de lo que se tiene")

    def ConsultarSaldo(self):
        return f"Saldo:{self.dinero}"


if __name__ == "__main__":
    #Create case of use 
    monedero = Monedero(100)
    print(monedero.ConsultarSaldo()) #100

    monedero.IngresoDinero(50)
    print(monedero.ConsultarSaldo()) #150

    monedero.RetirarDinero(20)
    print(monedero.ConsultarSaldo()) #130 Dinero retirado: 20. Saldo final:  None

    monedero.RetirarDinero(200)
    print(monedero.ConsultarSaldo())
