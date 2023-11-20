class LibreriaExternaMail():

    def __init__(self):
        pass

    def sendMail(self,destination,message,subject):
        print(f"To: {destination.getMail()}")
        print(f"Message: {message}")
        print(f"Subject: {subject}")
