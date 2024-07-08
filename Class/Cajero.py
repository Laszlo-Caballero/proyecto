import pickle
from .Movimiento import Movimiento
from .Usuario import Usuario
from .Billete import Billete


class Cajero:
    def __init__(self, Sucursal):
        self.Sucursal = Sucursal
        self.Estado = "A"
        self.Billetes = [Billete(200, 0), Billete(100, 0), Billete(50, 0), Billete(20, 0), Billete(10, 0)]
        with open("Data/Usuario.pkl", 'rb') as file:
            self.datos_cargados: list[Usuario] = pickle.load(file)
        self.DineroCajero = self.CargarDinero()

    def GuardarUsuario(self):
        with open('Data/Usuario.pkl', 'wb') as file:
            pickle.dump(self.datos_cargados, file)

    def Guardar(Cajeros):
        with open('Data/Cajero.pkl', 'wb') as file:
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
                print(self.Billetes[i].Cantidad)
                if self.Billetes[i].Cantidad > 0:
                    dinerototal = self.Billetes[i].Cantidad * self.Billetes[i].Valor
                    if dinerototal > cantidad:
                        dinero = cantidad // self.Billetes[i].Valor
                        if dinero > 0:
                            cantidad = cantidad % self.Billetes[i].Valor
                            listaBilletes.append(Billete(self.Billetes[i].Valor, dinero))
                            self.Billetes[i].Cantidad -= dinero
                            print("hola")
                    else:
                        listaBilletes.append(Billete(self.Billetes[i].Valor, self.Billetes[i].Cantidad))
                        cantidad -= dinerototal
                        self.Billetes[i].Cantidad = 0
        else:
            error = "No tiene la cantidad suficiente"
        
        
        Usuario.dinero -= auxcantidad
        Usuario.movimientos.append(Movimiento("0", Usuario.numeroCuenta, auxcantidad, "Retiro"))

        return error, listaBilletes
    
    def mostrar(self):
        for billete in self.Billetes:
            print(f"{billete.Cantidad=}, {billete.Valor=}")
