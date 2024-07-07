from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Class.Cajero import Cajero
import pickle
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
        
        self.selecCajero = -1

        with open('Data/Cajero.pkl', 'rb') as file:
            self.Cajeros : list[Cajero] = pickle.load(file) 

        self.btnFrame = Frame(self, bg='white')
        self.btnFrame.pack(expand=True)

        self.ImgAñadirOpen = Image.open("images/agregar-usuario.png") 
        self.ImgAñadir = ImageTk.PhotoImage(self.ImgAñadirOpen)
        self.BtnAñadir = ttk.Button(self.btnFrame, text ="Añadir Usuario" , image = self.ImgAñadir, compound=TOP, style='Rounded.TButton', command=self.AbrirVentanaAgregar)
        self.BtnAñadir.image = self.ImgAñadir
        self.BtnAñadir.pack(side='left')
        
        self.FrameMid = Frame(self.btnFrame, bg='white')

        self.txtVariableOpc = StringVar()
        self.CmbCajeros = ttk.Combobox(self.FrameMid, textvariable=self.txtVariableOpc, state='readonly')
        
        listaCajeros = []

        for cajero in self.Cajeros:
            listaCajeros.append(cajero.Sucursal)
        
        self.CmbCajeros['values'] = listaCajeros
        self.CmbCajeros.bind("<<ComboboxSelected>>", self.on_Change_ComboBox)

        self.CmbCajeros.pack()

        self.ImgCashOpen = Image.open("images/cash-report.png")
        self.ImgCash = ImageTk.PhotoImage(self.ImgCashOpen)
        self.BtnCash = ttk.Button(self.FrameMid, text ="Actualizar Dispensador" , image = self.ImgCash, compound=TOP, style='Rounded.TButton', command=self.AbrirVentanaActualizar)
        self.BtnCash.image = self.ImgCash
        self.BtnCash.pack(pady=(20,0))

        

        self.FrameMid.pack(side='left', padx=50)

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

    def on_Change_ComboBox(self, event):
        select = self.txtVariableOpc.get()

        for i in range(len(self.Cajeros)):
            if self.Cajeros[i].Sucursal == select:
                self.selecCajero = i 
        print(self.selecCajero)

def Main():
    app = MainPanel()
    app.mainloop()




py_hot_reload.run_with_reloader(Main)

