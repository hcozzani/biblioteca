from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def notificar(self,prestamo):
        pass