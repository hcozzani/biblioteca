from Modelo.Mail import Mail
from Modelo.LibreriaExternaMail import LibreriaExternaMail


class AdapterMail(Mail):
    
    def __init__(self):
        pass

    def enviarNotificacion(self, destino, mensaje, asusnto):
        LibreriaExternaMail().sendMail(destino,mensaje,asusnto)