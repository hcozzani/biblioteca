class LibreriaExternaSms():

    def __init__(self):
        pass


    def sendSms(self, destination, message, subject):
        print(f"To: {destination.getNumTelefono()}")
        print(f"Message: {message}")
        print(f"Subject: {subject}")
