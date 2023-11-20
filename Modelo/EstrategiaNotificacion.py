from abc import ABC, abstractmethod

class EstrategiaNotificacion(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def enviarNotificacion(self,destino, mensaje, asunto):
        pass