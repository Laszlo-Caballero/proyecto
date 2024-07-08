from tkinter import *
from Components.Header import Header
from Components.Saldo import Saldo
from Components.Botones import Botones
from Components.Boton import Boton
from .InterfazRetirar import Retirar
from Class.Usuario import Usuario
from Class.Cajero import Cajero
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
        self.header.pack()
        self.FrameMain = Frame(self, background='white')
        self.Saldo = Saldo(self.FrameMain,self.Usuario.numeroCuenta, self.Usuario.dinero, background='white')
        self.Saldo.pack(side='right', anchor='n', padx=(0,20))
        self.botones = Botones(self.FrameMain, [self.Retirar, self.Deposito, self.Transferencia, self.Servicios])
        self.botones.pack(side="left", padx=(20,0))
        self.FrameMain.pack(fill='x', pady=(20,0))
        self.prueba = Boton(self.FrameMain, text="Botón", image_path="images/retiro.png")
        self.prueba.pack(side='left', padx=(20, 0))
                

    
    def Retirar(self):
        print("Retirar")
        Retirar(self, self.Usuario, self.Cajero)
    def Deposito(self):
        print("Deposito")
    def Transferencia(self):
        print("Transferencia")
    def Servicios(self):
        print("Pagar Servicios")

        



