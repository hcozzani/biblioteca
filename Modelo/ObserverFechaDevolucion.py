from Modelo.Observer import Observer
from datetime import date, datetime
from Modelo.Notificacion import Notificacion


class ObserverFechaDevolucion(Observer):

    def __init__(self,prestamo):
        self.__prestamo = prestamo
        self.__fechaActual = datetime.today()
        #self.__fechaActual = datetime.combine(date.today(), datetime.min.time())
        self.__fechaVencimiento = prestamo.getFechaVencimiento()
        self.__diasRestantes = (prestamo.getFechaVencimiento() - datetime.today()).days
        self.__notificacion = Notificacion(prestamo.getCliente())
        #self.__notificacion = Notificacion(self.__prestamo.getCliente()) anterior a lo de arriba
        self.notificar()
        
    def notificar(self):
        self.__diasRestantes = (self.__fechaVencimiento - self.__fechaActual).days
        if 0 <= self.__diasRestantes <= 2:
            self.__notificacion.enviarNotificacion(self.__diasRestantes)

    def setFechaActual(self, nuevaFecha):
        self.__fechaActual = nuevaFecha
        self.notificar()

    def getDiasRestantes(self):
        return self.__diasRestantes