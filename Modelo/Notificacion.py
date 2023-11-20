class Notificacion():

    def __init__(self, clienteDestino):
        self.__destino = clienteDestino
        
    
    def getDestino(self): return self.__destino
    def setDestino(self): return self.__destino

    def enviarNotificacion(self,diasRestantes):
        mensaje = f"Hola, {self.__destino.getNombre()}. Quedan {diasRestantes}  dia/s para que entregues el ejemplar"
        asunto = "Vencimiento del ejemplar"
        self.__destino.getMedio().enviarNotificacion(self.__destino, asunto, mensaje)

