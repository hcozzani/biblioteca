from Modelo.EstrategiaNotificacion import EstrategiaNotificacion

class Sms(EstrategiaNotificacion):
    
    def __init__(self, adapterSms):
        self.__adapterSms = adapterSms

    def enviarNotificacion(self, destino, mensaje, asunto):
        self.__adapterSms.enviarNotificacion(destino,mensaje,asunto)