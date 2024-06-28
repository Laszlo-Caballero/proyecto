from Movimiento import Movimiento

class Usuario:
    def __init__(self, nombre, numeroCuenta, Dinero, Movimientos: list[Movimiento]= [], contraseña = ""):
        self.nombre = nombre
        self.numeroCuenta = numeroCuenta
        self.dinero = Dinero
        self.movimientos = Movimientos
        self.contraseña = contraseña

