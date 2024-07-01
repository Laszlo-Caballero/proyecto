from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import py_hot_reload
from Interface.InterfazAñadir import InterfazAñadir
from Interface.InterfazUsuario import Cuenta
from Interface.InterfazActualizarDepostio import InterfazActualizar


class MainPanel(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cajero")
        self.geometry("900x500")
        self.config(bg="white")
        
        self.btnFrame = Frame(self, bg='white')
        self.btnFrame.pack(expand=True)

        self.ImgAñadirOpen = Image.open("images/agregar-usuario.png") 
        self.ImgAñadir = ImageTk.PhotoImage(self.ImgAñadirOpen)
        self.BtnAñadir = ttk.Button(self.btnFrame, text ="Añadir Usuario" , image = self.ImgAñadir, compound=TOP, style='Rounded.TButton', command=self.AbrirVentanaAgregar)
        self.BtnAñadir.image = self.ImgAñadir
        self.BtnAñadir.pack(side='left')
        
        self.ImgCashOpen = Image.open("images/cash-report.png")
        self.ImgCash = ImageTk.PhotoImage(self.ImgCashOpen)
        self.BtnCash = ttk.Button(self.btnFrame, text ="Actualizar Dispensador" , image = self.ImgCash, compound=TOP, style='Rounded.TButton', command=self.AbrirVentanaActualizar)
        self.BtnCash.image = self.ImgCash
        self.BtnCash.pack(side='left', padx=50)

        self.ImgUsuarioOpen = Image.open("images/usuario.png")
        self.ImgUsuario = ImageTk.PhotoImage(self.ImgUsuarioOpen)
        self.BtnUsuario = ttk.Button(self.btnFrame, text="Interfaz Usuario", image= self.ImgUsuario, compound= TOP, style='Rounded.TButton', command=self.AbrirVentanaUsuario)
        self.BtnUsuario.image = self.ImgUsuario
        self.BtnUsuario.pack(side='right')
        

    def AbrirVentanaAgregar(self):
        InterfazAñadir(self)

    def AbrirVentanaActualizar(self):
        InterfazActualizar(self)

    def AbrirVentanaUsuario(self):
         Cuenta(self)

def Main():
    app = MainPanel()
    app.mainloop()




py_hot_reload.run_with_reloader(Main)

