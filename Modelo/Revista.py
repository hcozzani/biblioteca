from Modelo.Ejemplar import Ejemplar

class Revista(Ejemplar):

    def __init__(self, titulo, autor, fechaPublicacion, categoria):
        super().__init__(titulo, autor, fechaPublicacion, categoria)
        self.__diasDisponibles = 5

    def getDiasDisponibles(self):
        return self.__diasDisponibles
    
    def mostrarRevista(self):
        print(f"titulo: {self.getTitulo()} autor {self.getAutor()} fecha de publicacion {self.getFechaPublicacion()} categoria: {self.getCategoria()} dias disponibles {self.getDiasDisponibles()}")
