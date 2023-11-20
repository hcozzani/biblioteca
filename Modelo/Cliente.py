from Modelo.Habilitado import Habilitado
from Modelo.Suspendido import Suspendido
from Modelo.Sms import Sms
from Modelo.AdapterSms import AdapterSms
from Modelo.Mail import Mail
from Modelo.AdapterMail import AdapterMail

class Cliente:
    def __init__(self, nombre, apellido, dni, mail, numTelefono, medio):

        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__mail = mail
        self.__numTelefono = numTelefono
        if medio == "SMS": self.__medio = Sms(AdapterSms())
        elif medio == "MAIL": self.__medio = Mail(AdapterMail())
        else: print("El medio ingresado no es correcto")
        self.__listaPrestamo = []
        self.__estado = Habilitado(self)
        
        
    #Getter y Setter
    def getDni(self): return self.__dni
    
    def getNombre(self): return self.__nombre
    
    def getApellido(self): return self.__apellido
    
    def getEstado(self): return self.__estado

    def getMail(self): return self.__mail

    def getNumTelefono(self): return self.__numTelefono

    def getListaPrestamo(self): return self.__listaPrestamo

    def getMedio(self): return self.__medio
    

    def setNombre(self): return self.__nombre
    
    def setApellido(self): return self.__apellido
    
    def setDni(self): return self.__dni
    
    def setMail(self): return self.__mail
    
    def setNumTelefono(self): return self.__numTelefono

    def setEstado(self): return self.__estado
    

    #creo las funciones
    def solicitarPrestamo(self, ejemplar):
        self.getEstado().solicitarPrestamo(self,ejemplar)

    #chequeo la clase que esta bien
    def mostrarCliente(self):
        print(f"nombre: {self.__nombre}")
        print(f"apellido: {self.__apellido}")
        print(f"dni: {self.__dni}")
        print(f"mail: {self.__mail}")
        print(f"numTelefono: {self.__numTelefono}")

    def mostrarListaPrestamos(self):
        for prestamo in self.__listaPrestamo:
            prestamo.mostrarPrestamo()