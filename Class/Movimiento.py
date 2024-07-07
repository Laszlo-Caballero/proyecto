from datetime import datetime
import uuid

class Movimiento:
    def __init__(self, CuentaOrigen, CuentaDestino, Dinero, Tipo):
        self.NumeroOperacion = uuid.uuid1()
        self.CuentaOrigen = CuentaOrigen
        self.CuentaDestino = CuentaDestino
        self.Dinero = Dinero
        self.Tipo = Tipo
        self.Fecha = datetime.now()
