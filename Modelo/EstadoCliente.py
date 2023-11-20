from abc import ABC

class EstadoCliente(ABC):

    def __init__(self, cliente):
        self.__cliente = cliente
    
    def getCliente(self): 
        return self.__cliente
    
    def solicitarPrestamo(self):
        pass