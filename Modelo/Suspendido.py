from Modelo.EstadoCliente import EstadoCliente

class Suspendido(EstadoCliente):

    def __init__(self, cliente):
        super().__init__(cliente)
    
    def solicitarPrestamo(self,cliente, ejemplar):
        print(f"No se puede realizar el prestamo por que {cliente.getNombre()} {cliente.getApellido()} esta suspendido")