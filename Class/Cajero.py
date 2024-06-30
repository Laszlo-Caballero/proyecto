import pickle
from .Movimiento import Movimiento
from .Usuario import Usuario
from .Billete import Billete


class Cajero:
    def __init__(self, DineroCajero):
        self.DineroCajero = DineroCajero
        self.Billetes = [Billete(200, 100), Billete(100, 100), Billete(50, 100), Billete(20, 100)]
        with open("Data/Usuario.pkl", 'rb') as file:
            self.datos_cargados: list[Usuario] = pickle.load(file)

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

    def Depositar(self, CantidadDinero, CuentaDest):
        Encontrado = False
        Usuario = -1
        for i in range(0, len(self.datos_cargados)-1):
            if(CuentaDest == self.datos_cargados[i].numeroCuenta):
                Encontrado = True
                Usuario = i
                break
        if(Encontrado):
            print(f"Usuario = {self.datos_cargados[Usuario].nombre}")
            self.datos_cargados[Usuario].dinero += CantidadDinero
            NuevoMovimineto = Movimiento("Cajero", CuentaDest, CantidadDinero, "Deposito")
            self.datos_cargados[Usuario].movimientos.append(NuevoMovimineto)
            with open('Data/Usuario.pkl', 'wb') as file:
                pickle.dump(self.datos_cargados, file)
        else:
            print("Error al Encontrar Usuario")
    
    def Transferir(self, CantidadDinero, CuentaOrigen, CuentaDest):
        Origen = -1
        Dest = -1
        for i in range(0, len(self.datos_cargados)-1):
            if(CuentaOrigen == self.datos_cargados[i].numeroCuenta):
                Origen = i
                break
        if(Origen != -1 and self.datos_cargados[Origen].dinero >= CantidadDinero):
            for i in range(0, len(self.datos_cargados)-1):
                if(CuentaDest == self.datos_cargados[i].numeroCuenta):
                    Dest = i
                    break
            if(Dest != -1):
                NuevoMomiento = Movimiento(CuentaOrigen, CuentaDest, CantidadDinero, "Transferencia")
                if self.datos_cargados[Origen].dinero >= CantidadDinero:
                    self.datos_cargados[Origen].dinero -= CantidadDinero
                    self.datos_cargados[Origen].movimientos.append(NuevoMomiento)
                    self.datos_cargados[Dest].dinero += CantidadDinero
                    self.datos_cargados[Dest].movimientos.append(NuevoMomiento)
                    with open('Usuario.pkl', 'wb') as file:
                        pickle.dump(self.datos_cargados, file)
                else:
                    print("Error Al hacer el deposito")
            else:
                print("Error al encontrar El Destino")
        else:
            print("Error al Encontrar Usuario")

    def Guardar(self):
        with open('Data/Cajero.pkl', 'wb') as file:
            pickle.dump(self, file)
        with open('Data/Usuario.pkl', 'wb') as file:
            pickle.dump(self.datos_cargados, file)

    def AñadirDinero(self, Cantidad, Billetes: list[Billete]):
        self.DineroCajero += Cantidad
        for i in range(0, len(self.Billetes)-1):
            self.Billetes[i].Cantidad += Billetes[i].Cantidad
              


# with open('Data/Cajero.pkl', 'rb') as file:
#      cajero: Cajero = pickle.load(file) 



# # billetes :list[Billete] = cajero.SacarDinero(1100)

# # cajero.Guardar()

# # for billete in billetes:
# #     print(f"Billete: {billete.Valor} Cantidad: {billete.Cantidad}")

# for i in range(0, len(cajero.Billetes) -1):
#     print(f"{cajero.Billetes[i].Valor=}  {cajero.Billetes[i].Cantidad=}")