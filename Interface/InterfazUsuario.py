from tkinter import *
from Components.Header import Header
from Components.Saldo import Saldo
from Components.Botones import Botones
from Components.Boton import Boton
from .InterfazRetirar import Retirar
from Class.Usuario import Usuario
from Class.Cajero import Cajero
from Components.FMovimiento import FMovimiento
from .InterfazMovimientos import InterfazMovmientos
# import py_hot_reload

class Cuenta(Toplevel):
    def __init__(self, parent, Usuario: Usuario, Cajero: Cajero):
        super().__init__(parent)
        self.Usuario = Usuario
        self.Cajero = Cajero
        self.NombreSucursal = ""
        self.title("Cuenta Usuario")
        self.geometry("900x500")
        self.config(bg="white")
        self.header = Header(self, self.Usuario.nombre)
        self.header.pack(fill='x')

        self.FramePrincipal = Frame(self, background='white')
        self.FramePrincipal.pack(expand=True, fill='both')

        self.FrameDerecha = Frame(self.FramePrincipal, background='white')
        self.FrameDerecha.pack(side='right', expand=True, fill='both', pady=(10,0))

        self.Saldo = Saldo(self.FrameDerecha, self.Usuario.numeroCuenta, self.Usuario.dinero, background='white')
        self.Saldo.pack()

        self.FrameMovimiento = Frame(self.FrameDerecha, bg='white')
        
        for mv in range(len(self.Usuario.movimientos)):
                FMovmieto = FMovimiento(self.FrameMovimiento, self.Usuario.movimientos[mv])
                FMovmieto.grid(row=mv//2, column=mv%2, sticky='w')
                if mv == 9:
                     break

        self.FrameMovimiento.pack(fill='both', padx=(20,0), pady=(10,0))

        self.botones = Botones(self.FramePrincipal, [self.Retirar, self.Deposito, self.Transferencia, self.Servicios, self.VerMovimientos])
        self.botones.pack(side='top')
    
    def Retirar(self):
        print("Retirar")
        Retirar(self, self.Usuario, self.Cajero)
    def Deposito(self):
        print("Deposito")
    def Transferencia(self):
        print("Transferencia")
    def Servicios(self):
        print("Pagar Servicios")
    def VerMovimientos(self):
         InterfazMovmientos(self, self.Usuario.movimientos, self.Usuario.nombre)

        



