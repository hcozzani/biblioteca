from Modelo.EstrategiaNotificacion import EstrategiaNotificacion

class Mail(EstrategiaNotificacion):
    
    def __init__(self, adapterMail):
        self.__adapterMail = adapterMail

    def enviarNotificacion(self, destino, mensaje, asunto):
        self.__adapterMail.enviarNotificacion(destino,mensaje,asunto)