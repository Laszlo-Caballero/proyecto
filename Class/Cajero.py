class Cajero:
    def __init__(self):
        self.DineroIncial = 1500
        self.DineroCajero = 20000
    def SacarDinero(self, cantidad):
        if(self.DineroIncial > cantidad and self.DineroCajero > cantidad):
            self.DineroIncial = self.DineroIncial- cantidad
            return True
        else:
            return False
    def Depositar(self, cantidad):
        self.DineroCajero = self.DineroCajero + cantidad
        self.DineroIncial = self.DineroIncial + cantidad
    def Transferencia(self, numeroCuenta):
        pass
    def PagarServicio(self, servicio):
        pass
    

cajero = Cajero()

if cajero.SacarDinero(1200):
    print(cajero.DineroIncial)
    print("se saco")
else:
    print("no saco")