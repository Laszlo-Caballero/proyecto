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
from .InterfazTranferencia import InterfazTransferencia
import pickle
# import py_hot_reload

class Cuenta(Toplevel):
    def __init__(self, parent, usuario: Usuario, Cajero: Cajero):
        super().__init__(parent)
        self.Usuario = usuario
        self.Cajero = Cajero
        self.NombreSucursal = ""
        self.title("Cuenta Usuario")
        self.geometry("900x500")
        self.config(bg="white")
        self.header = Header(self, self.Usuario.nombre)
        self.header.pack(fill='x')

        self.idxUsuario = -1
        with open("Data/Usuario.pkl", 'rb') as file:
            self.Usuarios: list[Usuario] = pickle.load(file)

        self.FramePrincipal = Frame(self, background='white')
        self.FramePrincipal.pack(expand=True, fill='both')

        for i in range(len(self.Usuarios)):
             if self.Usuarios[i].dni == self.Usuario.dni:
                self.idxUsuario = i
                break

        self.FrameDerecha = Frame(self.FramePrincipal, background='white')
        self.FrameDerecha.pack(side='right', expand=True, fill='both', pady=(10,0))

        self.Saldo = Saldo(self.FrameDerecha, self.Usuarios[self.idxUsuario].numeroCuenta, self.Usuarios[self.idxUsuario].dinero, background='white')
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
        top = Retirar(self, self.Usuario, self.Cajero)
        top.protocol("WM_DELETE_WINDOW", lambda: self.on_toplevel_close(top))

    def on_toplevel_close(self, top: Toplevel):
        top.destroy()
        self.CargarDatos()
        print(self.Usuarios[self.idxUsuario].dinero)
        self.Saldo.Actualizar(self.Usuarios[self.idxUsuario].dinero)
    
    def CargarDatos(self):
        with open("Data/Usuario.pkl", 'rb') as file:
            self.Usuarios: list[Usuario] = pickle.load(file)

    def Deposito(self):
        print("Deposito")
    def Transferencia(self):
        print("Transferencia")
        top = InterfazTransferencia(self, self.Usuario)
        top.protocol("WM_DELETE_WINDOW", lambda: self.on_toplevel_close(top))

    def Servicios(self):
        print("Pagar Servicios")
    def VerMovimientos(self):
         InterfazMovmientos(self, self.Usuarios[self.idxUsuario].movimientos, self.Usuarios[self.idxUsuario].nombre)

        



