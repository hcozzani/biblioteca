from Modelo.EstadoCliente import EstadoCliente
from Modelo.Prestamo import Prestamo

class Habilitado(EstadoCliente):

    def __init__(self, cliente):
        super().__init__(cliente)

    def solicitarPrestamo(self,cliente, ejemplar):
        if ejemplar.isDisponible():
            cliente.getListaPrestamo().append(Prestamo(ejemplar,cliente))
            ejemplar.setDisponible(False)
        else:
            print(f"El ejemplar {ejemplar.getTitulo()} no esta disponible")
        
        
    