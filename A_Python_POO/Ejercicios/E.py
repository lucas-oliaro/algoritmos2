"""Una cadena de restaurantes llamada "Delicioso Sabor" desea implementar un sistema de gestión de pedidos
automatizado para mejorar la eficiencia en el manejo de sus ventas y optimizar el control de su inventario.
Requerimientos del Sistema:
1. Clase Producto:
○ Cada producto en el menú del restaurante debe ser representado por la clase Producto.
○ Los productos deben tener un nombre, precio unitario y cantidad inicial en stock.
○ Se debe poder actualizar la cantidad en stock de cada producto conforme se realicen pedidos.
2. Clase Pedido:
○ La clase Pedido debe registrar los detalles de cada pedido realizado por los clientes.
○ Cada pedido debe contener un número único de identificación, una lista de productos solicitados y su
estado actual.
○ Se debe calcular el costo total del pedido, aplicando un descuento global del 10% por defecto.
○ Se debe poder actualizar el estado de los pedidos a medida que progresan en su preparación y
entrega."""

class Producto():
    def __init__(self,nombre: str, precio: float, cantidadStock: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidadStock = cantidadStock

    def ActualizacionStockProducto(self, amount: int):
        self.cantidadStock = self.cantidadStock - amount

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.cantidadStock}"


class Pedido():
    i=1000
    def IDGenerator(self):
        Pedido.i += 1
        return Pedido.i

    def __init__(self,ID: int, ProductosSolicitados: list):
        self.ID = Pedido.IDGenerator(self)
        self.ProductosSolicitados = ProductosSolicitados
        self.situacionPedido = "Ingresado"

    def ListPreciosProductos(self, producto):
        precios = {
            "Hamburgesa": 5.00,
            "Papas": 2.00,
            "Pizza": 7.00,
            "Refresco": 1.50
        }
        return precios[producto]

    def CostoPedido(self):
        total = 0
        for producto in self.ProductosSolicitados:
            total += producto.precio
        return total
    

    def DescuentoPedido(self):
        return self.CostoPedido() * 0.10
    
    def PrecioFinalPedido(self):
        return self.CostoPedido() - self.DescuentoPedido()


    def ProgresoPedido(self):
        situaciones = ["Ingresado", "En Preparacion", "En Camino", "Entregado"]

        situacionPedido = self.situacionPedido
        index = situaciones.index(situacionPedido)
        self.situacionPedido = situaciones[index+1]
        return self.situacionPedido


    def ActualizacionSituacionPedido(self):
        self.situacionPedido = self.ProgresoPedido()


    
