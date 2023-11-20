from Modelo.Ejemplar import Ejemplar
from Modelo.Libro import Libro
from Modelo.Diario import Diario
from Modelo.Revista import Revista
import pymongo

class ControllerEjemplar:
    __instance = None
    __listaEjemplar = []

    #patron singletone
    def __new__(cls):
        if ControllerEjemplar.__instance is None:
            ControllerEjemplar.__instance = object.__new__(cls)
        return ControllerEjemplar.__instance
    
    def altaEjemplar(self,tipo,titulo, autor, fechaPublicacion, categoria):
        #hago el alta del ejemplar en la lista
        if tipo == "Libro": ejemplar = Libro(titulo, autor, fechaPublicacion, categoria)
        elif tipo == "Diario": ejemplar = Diario(titulo, autor, fechaPublicacion, categoria)
        elif tipo == "Revista": ejemplar = Revista(titulo, autor, fechaPublicacion, categoria)
        else:
            print("No existe ese tipo de ejemplar")
         
        self.__listaEjemplar.append(ejemplar)

        e = pymongo.MongoClient(serverSelectionTimeoutMS = 1000)
        db = e.get_database("Biblioteca")
        coleccionEjemplares = db.get_collection("Ejemplares")

        try:
            coleccionEjemplares.insert_one(({"titulo": titulo, "_id": {"_titulo": titulo},
                                          "autor": autor, "fechaPublicacion": fechaPublicacion, 
                                          "categoria": categoria}))
        except pymongo.errors.DuplicateKeyError:
            print("Ya existe ese titulo")


    #modificar ejemplares en mongo db
    def modificarEjemplar(self, titulo,autor,fechaPublicacion, categoria):
        e = pymongo.MongoClient(serverSelectionTimeoutMS = 1000)
        db = e.get_database("Biblioteca")
        coleccionEjemplares = db.get_collection("Ejemplares")

        filtro = {"titulo": titulo}
        actualizacion = {
            "$set": {
                "autor": autor,
                "fechaPublicacion": fechaPublicacion,
                "categoria": categoria
            }
        }

        resultado = coleccionEjemplares.update_one(filtro, actualizacion)

        if resultado.modified_count > 0:
            print("Registro del ejemplar modificado con éxito")

    def bajaEjemplar(self,titulo):
        #hago la baja del cliente
        e = self.getEjemplaresByTitulo(titulo)

        e = pymongo.MongoClient(serverSelectionTimeoutMs = 1000)
        db = e.get_database("Biblioteca")
        coleccionEjemplares = db.get_collection("Ejemplares")
        ejemplares_a_eliminar = {"titulo": titulo}
        coleccionEjemplares.delete_one(ejemplares_a_eliminar)
        print(f"titulo: {titulo} eliminado")

    def getEjemplaresByTitulo(self, titulo):
        for ejemplar in self.__listaEjemplar:
            if ejemplar.getTitulo() == titulo: 
                return ejemplar
        
    def mostrarEjemplares(self):
        for ejemplar in self.__listaEjemplar:
            ejemplar.mostrarEjemplar()

    def mostrarEjemplarByTitulo(self, titulo):
        ejemplar = self.getEjemplaresByTitulo(titulo)
        ejemplar.mostrarEjemplar()
    
