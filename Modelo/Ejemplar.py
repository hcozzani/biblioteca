from abc import ABC, abstractmethod

class Ejemplar(ABC):

    def __init__(self, titulo, autor, fechaPublicacion, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__fechaPublicacion = fechaPublicacion
        self.__categoria = categoria
        self.__disponible = True

    #@abstractmethod
    def getTitulo(self): return self.__titulo
    
    def getAutor(self): return self.__autor
    
    def getFechaPublicacion(self): return self.__fechaPublicacion
    
    def getCategoria(self): return self.__categoria

    def isDisponible(self): return self.__disponible
    
    def setTitulo(self): return self.__titulo
    
    def setAutor(self): return self.__autor
    
    def setFechaPublicacion(self, fechaPublicacion): self.__fechaPublicacion = fechaPublicacion
    
    def setCategoria(self): return self.__categoria

    def setDisponible(self,value): self.__disponible = value 
    


    def busquedaEjemplar(self):
        pass
    

    def getDiasDisponibles(self): ##modifique aca le puse 0 por que none no es valido, despues lo sobre escribe
        return 0

        #chequeo la clase que esta bien
    def mostrarEjemplar(self):
        print(f"titulo: {self.__titulo}")
        print(f"autor: {self.__autor}")
        print(f"fechaPublicacion: {self.__fechaPublicacion}")
        print(f"categoria: {self.__categoria}")
        print(f"disponible: {self.__disponible}")