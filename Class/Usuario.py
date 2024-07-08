from .Movimiento import Movimiento
import pickle
class Usuario:
    def __init__(self, nombre, dni, numeroCuenta, Dinero, Movimientos: list[Movimiento]= [], contraseña = ""):
        self.nombre = nombre
        self.dni = dni
        self.numeroCuenta = numeroCuenta
        self.dinero = Dinero
        self.movimientos = Movimientos
        self.contraseña = contraseña

    def Guardar(Usuarios):
        with open(r'Data/Usuario.pkl', 'wb') as file:
            pickle.dump(Usuarios, file)