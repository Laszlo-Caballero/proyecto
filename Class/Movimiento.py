from datetime import datetime

class Movimiento:
    def __init__(self, CuentaOrigen, CuentaDestino, Dinero, Tipo):
        self.CuentaOrigen = CuentaOrigen
        self.CuentaDestino = CuentaDestino
        self.Dinero = Dinero
        self.Tipo = Tipo
        self.Fecha = datetime.now()