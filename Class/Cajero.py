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
        auxcantidad = cantidad
        error = ""
        if(cantidad <= Usuario.dinero):
            for i in range(len(self.Billetes)):
                print(f"{self.Billetes[i].Cantidad=}")
                if self.Billetes[i].Cantidad > 0:
                    dinerototal = self.Billetes[i].Cantidad * self.Billetes[i].Valor

                    if dinerototal > cantidad:
                        dinero = cantidad // self.Billetes[i].Valor
                    
                        if dinero > 0:
                            cantidad = cantidad % self.Billetes[i].Valor
                            listaBilletes.append(Billete(self.Billetes[i].Valor, dinero))
                            self.Billetes[i].Cantidad -= dinero
                    else:
                        listaBilletes.append(Billete(self.Billetes[i].Valor, self.Billetes[i].Cantidad))
                        cantidad -= dinerototal
                        self.Billetes[i].Cantidad = 0
                elif cantidad == 0:
                    break 
                else:
                    error = "No hay billetes suficientes"
        else:
            error = "No tiene la cantidad suficiente"

        if error == "":
            Usuario.dinero -= auxcantidad
            Usuario.movimientos.append(Movimiento("0", Usuario.numeroCuenta, auxcantidad, "Retiro"))

        return error, listaBilletes

    def Transferencia(cantidad: int, Usuario: Usuario, receptor: Usuario):
        error = ""
        if cantidad <= Usuario.dinero:
           Usuario.dinero -= cantidad
           receptor.dinero += cantidad
        else:
            error = "No tiene el dinero suficiente"     

        if error == "":
            Usuario.movimientos.append(Movimiento(Usuario.numeroCuenta, receptor.numeroCuenta, cantidad, f"Transferencia a {receptor.numeroCuenta}"))
            receptor.movimientos.append(Movimiento(Usuario.numeroCuenta, receptor.numeroCuenta, cantidad, f"Transferencia de {Usuario.numeroCuenta}"))

        return error