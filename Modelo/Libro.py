from Modelo.Ejemplar import Ejemplar

class Libro (Ejemplar):

    def __init__(self, titulo, autor, fechaPublicacion, categoria):
        super().__init__(titulo, autor, fechaPublicacion, categoria)
        self.__diasDisponibles = 10

    def getDiasDisponibles(self):
        return self.__diasDisponibles

    def mostrarLibro(self):
        print(f"titulo: {self.getTitulo()} autor: {self.getAutor()} fecha de publicacion: {self.getFechaPublicacion()} categoria: {self.getCategoria()} dias disponibles: {self.getDiasDisponibles()}")
