

class Cajero:
    def __init__(self):
        self.DineroIncial = 1500
    def SacarDinero(self, cantidad):
        if(self.DineroIncial > cantidad):
            self.DineroIncial = self.DineroIncial- cantidad
            return True
        else:
            return False
    def Depositar(self, cantidad):
        self.DineroIncial = self.DineroIncial + cantidad
    


cajero = Cajero()

if cajero.SacarDinero(1200):
    print(cajero.DineroIncial)
    print("se saco")
else:
    print("no saco")