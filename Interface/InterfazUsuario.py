from tkinter import *
from Components.Header import Header
from Components.Saldo import Saldo
from Components.Botones import Botones
from Components.Boton import Boton
# import py_hot_reload

class Cuenta(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cuenta Usuario")
        self.geometry("900x500")
        self.config(bg="white")
        self.header = Header(self, width=500)
        self.header.pack()
        self.FrameMain = Frame(self, background='white')
        self.Saldo = Saldo(self.FrameMain, background='white')
        self.Saldo.pack(side='right', anchor='n', padx=(0,20))
        self.botones = Botones(self.FrameMain)
        self.botones.pack(side="left", padx=(20,0))
        self.FrameMain.pack(fill='x', pady=(20,0))
        self.prueba = Boton(self.FrameMain, text="Botón", image_path="images/retiro.png")
        self.prueba.pack(side='left', padx=(20, 0))
                


        



