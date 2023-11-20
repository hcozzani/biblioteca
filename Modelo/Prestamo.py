from Modelo.ObserverFechaDevolucion import ObserverFechaDevolucion
from datetime import datetime, timedelta


class Prestamo:

    def __init__(self, ejemplar, cliente):
        self.__fechaInicio = datetime.today()
        self.__fechaVencimiento = self.__fechaInicio + timedelta(ejemplar.getDiasDisponibles())
        self.__ejemplar = ejemplar
        self.__cliente = cliente
        self.__observerFechaDevolucion = ObserverFechaDevolucion(self)

    def getFechaInicio(self): return self.__fechaInicio
    def getEjemplar(self): return self.__ejemplar
    def getFechaVencimiento(self): return self.__fechaVencimiento
    def getCliente(self): return self.__cliente
    def getObserverFechaDevolucion(self): return self.__observerFechaDevolucion
 

    def agregar_observer(self, observer):
        ##self.__listaObserver.append(observer) antes!!
        self.__observer.append(observer) #nuevo

    def eliminar_observer(self,observer):
        #self.__listaObserver.remove(observer) antes!!
        self.__observer.remove(observer) #nuevo

    def notificar_observadores(self): ##nuevo esto
        for observer in self.__observer:
            observer.notificar(self)

    def mostrarPrestamo(self):
        print(f"{self.getEjemplar().getTitulo()}\t\t{self.__fechaInicio}\t{self.__fechaVencimiento}")


