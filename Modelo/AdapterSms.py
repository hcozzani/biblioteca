from Modelo.Sms import Sms
from Modelo.LibreriaExternaSms import LibreriaExternaSms

class AdapterSms(Sms):
    
    def __init__(self):
        pass

    def enviarNotificacion(self, destino, mensaje, asusnto):
        LibreriaExternaSms().sendSms(destino,mensaje,asusnto)