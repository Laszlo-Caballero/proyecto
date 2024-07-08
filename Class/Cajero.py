import pickle
from .Movimiento import Movimiento
from .Usuario import Usuario
from .Billete import Billete


class Cajero:
    def __init__(self, Sucursal):
        self.Sucursal = Sucursal
        self.Estado = "A"
        self.Billetes = [Billete(200, 0), Billete(100, 0), Billete(50, 0), Billete(20, 0), Billete(10, 0)]
        with open(r"Data/Usuario.pkl", 'rb') as file:
            self.datos_cargados: list[Usuario] = pickle.load(file)
        self.DineroCajero = self.CargarDinero()

    def SacarDinero(self, Dinero):
        CantBilletes = []
        if(self.DineroCajero >= Dinero):
            for i in range(0, len(self.Billetes)-1):
                division = Dinero // self.Billetes[i].Valor
                if division >= 1:
                    CantBilletes.append(Billete(self.Billetes[i].Valor, division))
                    self.Billetes[i].Cantidad -= division
                Dinero = Dinero % self.Billetes[i].Valor

        self.DineroCajero -= Dinero
        self.Guardar()
        return CantBilletes

    def GuardarUsuario(self):
        with open(r'Data/Usuario.pkl', 'wb') as file:
            pickle.dump(self.datos_cargados, file)

    def Guardar(Cajeros):
        with open(r'Data/Cajero.pkl', 'wb') as file:
            pickle.dump(Cajeros, file)

    def AñadirDinero(self,BilletesNuevos: Billete):
        for i in range(len(self.Billetes)):
            if self.Billetes[i].Valor == BilletesNuevos.Valor:
                self.Billetes[i].Cantidad += BilletesNuevos.Cantidad
                break
        self.DineroCajero = self.CargarDinero()
        
    def CargarDinero(self):
        dinero = 0
        for billete in self.Billetes:
            dinero += billete.Cantidad * billete.Valor
        return dinero
    
    def RetirarDinero(self, cantidad, Usuario: Usuario):
        listaBilletes = []
        if(cantidad <= Usuario.dinero):
            for billete in self.Billetes:
                print(billete.Cantidad)
                if billete.Cantidad > 0:
                    dinerototal = billete.Cantidad * billete.Valor
                    if dinerototal > cantidad:
                        dinero = cantidad // billete.Valor
                        if dinero > 0:
                            cantidad = cantidad % billete.Valor
                            listaBilletes.append(Billete(billete.Valor, dinero))
                            billete.Cantidad -= dinero
                    else:
                        listaBilletes.append(Billete(billete.Valor, billete.Cantidad))
                        cantidad -= dinerototal
                        billete.Cantidad = 0
                    
                elif cantidad == 0:
                    break 
        return listaBilletes
