from datetime import datetime

class Transferencia:
    def __init__(self, CuentaOrigen, CuentaDestino, Dinero):
        self.CuentaOrigen = CuentaOrigen
        self.CuentaDestino = CuentaDestino
        self.Dinero = Dinero
        self.Fecha = datetime.now()