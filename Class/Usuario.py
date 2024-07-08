from .Movimiento import Movimiento

class Usuario:
    def __init__(self, nombre, dni, numeroCuenta, Dinero, Movimientos: list[Movimiento]= [], contraseña = ""):
        self.nombre = nombre
        self.dni = dni
        self.numeroCuenta = numeroCuenta
        self.dinero = Dinero
        self.movimientos = Movimientos
        self.contraseña = contraseña

