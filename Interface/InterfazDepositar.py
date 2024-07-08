from tkinter import Toplevel
from Class.Usuario import Usuario
from Class.Cajero import Cajero
import pickle


class InterfazDepositar(Toplevel):
    def __init__(self, parent, usuario: Usuario, cajero: Cajero = None):
        super().__init__(parent)
        self.title("Depositar")
        self.geometry("900x500")
        self.Usuario = usuario
        self.Cajero = cajero
        with open(r'Data/Cajero.pkl', 'rb') as file:
            self.Cajeros : list[Cajero] = pickle.load(file)
        with open(r"Data/Usuario.pkl", 'rb') as file:
            self.Usuarios: list[Usuario] = pickle.load(file) 
        
        self.IdxUsuario = -1
        self.selecCajero = -1

        for i in range(len(self.Cajeros)):
            if self.Cajeros[i].Sucursal == self.Cajero.Sucursal:
                self.selecCajero = i
                break
        for i in range(len(self.Usuarios)):
            if self.Usuarios[i].numeroCuenta == self.Usuario.numeroCuenta:
                self.IdxUsuario = i
