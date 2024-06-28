from tkinter import *
from Components.Header import Header
from Components.Saldo import Saldo
from Components.Boton import Boton
import py_hot_reload

class Cuenta(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cajero")
        self.geometry("900x500")
        self.config(bg="white")
        self.header = Header(self, width=500)
        self.header.pack()
        self.FrameMain = Frame(self, background='white')
        self.Saldo = Saldo(self.FrameMain, background='white')
        self.Saldo.pack(side='right', anchor='n', padx=(0,20))
        self.botones = Boton(self.FrameMain)
        self.botones.pack(side="left", padx=(20,0))
        self.FrameMain.pack(fill='x', pady=(20,0))


def Main():
    app = Cuenta()
    app.mainloop()
py_hot_reload.run_with_reloader(Main)