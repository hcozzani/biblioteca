from Controlador.ControllerCliente import ControllerCliente
from Controlador.ControllerEjemplar import ControllerEjemplar


cc = ControllerCliente()
ce = ControllerEjemplar()

cc.altaCliente("Elias","Gonzalez","13","pepe@hotmail.com","1111111","Mail")
cc.altaCliente("aaaa","Gonzalez","11","pepe@hotmail.com","1111111","SMS")
cc.altaCliente("aaaa","Gonzalez","12","pepe@hotmail.com","1111111","SMS")
#cc.altaCliente("Hugo","Gonzalez","3","juanperez@gmail.com","03456","Mail")
#cc.bajaCliente("1")
#cc.modificarCliente("1","Lucas","Navarro","mailmail","11111111","sms")

#cc.mostrarClientes()
#cc.habilitarCliente("Pepe","1")
#cc.mostrarClientes()
#cc.mostrarClienteByDni("34.958.321") 


ce.altaEjemplar("Libro","Prog 3","Juan Jimenez","01-01-14","Novela")
ce.altaEjemplar("Libro","Prog 5","Juan Jimenez","01-01-14","Novela")
ce.altaEjemplar("Libro","Prog 6","Juan Jimenez","01-01-14","Novela")
ce.altaEjemplar("Libro","Prog 7","Juan Jimenez","01-01-14","Novela")
#ce.altaEjemplar("Programacion 3","Guido Castro","20-12-22","Tecnico")
#ce.modificarEjemplar("Pro 3", "lalal", "2020", "Policiales")
#ce.bajaEjemplar("Platero 2")
#ce.mostrarEjemplares()

#cc.getClienteByDni("1").getEstado().solicitarPrestamo("Platero y Yo")

# ce.mostrarEjemplares() 

# ce.mostrarEjemplarByTitulo("Platero")


########## Pruebo el observer
""" 
cliente = cc.getClienteByDni("8")
ejemplar = ce.getEjemplaresByTitulo("Prog 2")
fecha_vencimiento = datetime(2023, 10, 22)  # Establece una fecha de vencimiento cercana
prestamo = Prestamo(ejemplar, cliente)

observador_fecha_devolucion = ObserverFechaDevolucion(prestamo)
prestamo.agregar_observer(observador_fecha_devolucion)


cc.avanzarFecha(datetaime(2023, 10, 20))

 """

cc.solicitarPrestamo("13",ce.getEjemplaresByTitulo("Prog 7"))