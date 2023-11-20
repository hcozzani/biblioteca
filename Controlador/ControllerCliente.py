from Modelo.Cliente import Cliente
from Modelo.Habilitado import Habilitado
from Modelo.Suspendido import Suspendido
import pymongo

class ControllerCliente():
    __instance = None
    __listaCliente = []
    #__listaPrestamo = []

    #patron singleton
    def __new__(cls):
        if ControllerCliente.__instance is None:
            ControllerCliente.__instance = object.__new__(cls)
        return ControllerCliente.__instance
    
    def habilitarCliente(self, dni):
        cliente = self.getClienteByDni(dni)
        cliente.setEstado(Habilitado(cliente))
         
    def suspenderCliente(self, dni):
        cliente = self.getClienteByDni(dni)
        print(f"El cliente {cliente.getNombre()} {cliente.getApellido()} ha sido suspendido")
        cliente.setEstado(Suspendido(cliente))

    def altaCliente(self,nombre, apellido, dni, mail, telefono, medio):
        #hago el alta del cliente
        cliente = Cliente(nombre, apellido, dni, mail, telefono, medio)
        self.__listaCliente.append(cliente)

        c = pymongo.MongoClient(serverSelectionTimeoutMS = 1000)
        db = c.get_database("Biblioteca")
        coleccionClientes = db.get_collection("Clientes")

        try:
            coleccionClientes.insert_one({"nombre": nombre, "_id": {"_dni": dni},
                                          "apellido": apellido, "dni": dni, "mail": mail, "telefono": telefono, "medio": medio})
        except pymongo.errors.DuplicateKeyError:
            print("Ya existe el dni")


    def modificarCliente(self, dni,nombre, apellido, mail, telefono, medio):
        c = pymongo.MongoClient(serverSelectionTimeoutMS = 1000)
        db = c.get_database("Biblioteca")
        coleccionClientes = db.get_collection("Clientes")

        filtro = {"dni": dni}
        actualizacion = {
            "$set": {
                "nombre": nombre,
                "apellido": apellido,
                "mail": mail,
                "telefono": telefono,
                "medio": medio
            }
        }

        resultado = coleccionClientes.update_one(filtro, actualizacion)

        if resultado.modified_count > 0:
            print("Registro del cliente modificado con éxito")


    def bajaCliente(self,dni): 
        #hago la baja del cliente
        #for cliente in self.__listaCliente:
            #if cliente.getDni() == dni:
                #self.__listaCliente.remove(cliente)

        c = pymongo.MongoClient(serverSelectionTimeoutMs = 1000)
        db = c.get_database("Biblioteca")
        coleccionClientes = db.get_collection("Clientes")
        cliente_a_eliminar = {"dni": dni}
        coleccionClientes.delete_one(cliente_a_eliminar)
        print(f"dni: {dni} eliminado")

    def getClienteByDni(self, dni):
        # for cliente in self.__listaCliente:
        #     if cliente.getDni() == dni: 
        #         return cliente
            
        c = pymongo.MongoClient(serverSelectionTimeoutMs = 1000)
        db = c.get_database("Biblioteca")
        coleccionClientes = db.get_collection("Clientes")
        cliente_a_mostrar = {"dni": dni}
        coleccionClientes.delete_one(cliente_a_mostrar)
        print(f"dni: {dni} mostrado")
        
    def mostrarListaPrestamo(self): 
        for prestamo in self.__listaPrestamo:
            prestamo.mostrarPretsamo()


    def solicitarPrestamo(self, dni, ejemplar):
        cliente = self.getClienteByDni(dni)
        cliente.solicitarPrestamo(ejemplar)


    def mostrarClientes(self):
        for cliente in self.__listaCliente:
            cliente.mostrarCliente()
        

    def mostrarClienteByDni(self, dni):
        cliente = self.getClienteByDni(dni)
        cliente.mostrarCliente()

    def mostrarHistorialPrestamo(self, dni):
        cliente = self.getClienteByDni(dni)
        cliente.mostarListaPrestamo()


    #metodo para avanzar fecha del observer
    def avanzarFecha(self,fechaNueva):
        for cliente in self.__listaCliente:
            for prestamo in cliente.getListaPrestamo():
                prestamo.getObserverFechaDevolucion().setFechaActual(fechaNueva)