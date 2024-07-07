from tkinter import messagebox, Tk, Frame, StringVar, TOP, Toplevel
from tkinter import ttk
from PIL import Image, ImageTk
from Class.Cajero import Cajero
import pickle
# import py_hot_reload
from Interface.InterfazAñadir import InterfazAñadir
from Interface.InterfazUsuario import Cuenta
from Interface.InterfazActualizarDepostio import InterfazActualizarDepostio
from Interface.InterfazAñadirCajero import AñadirCajero
from Components.Boton import Boton

class MainPanel(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cajero")
        self.geometry("900x500")
        self.config(bg="white")
        
        self.selecCajero = -1

        with open('Data/Cajero.pkl', 'rb') as file:
            self.Cajeros : list[Cajero] = pickle.load(file) 

        self.FramePrincipal = Frame(self, bg='white')
        self.FramePrincipal.pack(expand=True)
        
        self.txtVariableOpc = StringVar()
        self.CmbCajeros = ttk.Combobox(self.FramePrincipal, textvariable=self.txtVariableOpc, state='readonly')
        
        self.listaCajeros = []

        for cajero in self.Cajeros:
            self.listaCajeros.append(cajero.Sucursal)
        self.listaCajeros.append("Agregar Cajero")
        
        self.CmbCajeros['values'] = self.listaCajeros
        self.CmbCajeros.bind("<<ComboboxSelected>>", self.on_Change_ComboBox)

        self.CmbCajeros.pack(pady=(0,20))

        self.btnFrame = Frame(self.FramePrincipal, bg='white')
        self.btnFrame.pack()



        self.BtnAñadir = Boton(self.btnFrame, text ="Añadir Usuario" , image_path= "images/agregar-usuario.png", command=self.AbrirVentanaAgregar)
        self.BtnAñadir.pack(side='left')

        self.BtnCash = Boton(self.btnFrame, text ="Actualizar Dispensador" , image_path= "images/cash-report.png", command=self.AbrirVentanaActualizar)
        self.BtnCash.pack(side='left', padx=50)

        self.BtnUsuario = Boton(self.btnFrame, text="Interfaz Usuario", image_path="images/usuario.png", command=self.AbrirVentanaUsuario )
        self.BtnUsuario.pack(side='right')
        
        

    def AbrirVentanaAgregar(self):
        InterfazAñadir(self)

    def AbrirVentanaActualizar(self):
        if self.selecCajero != -1:
            InterfazActualizarDepostio(self, self.selecCajero)
        else:
            messagebox.showerror("Error", "Tienes que elejir un cajero de alguna sucursal")
    
    def AbrirVentanaUsuario(self):
        Cuenta(self)

    def on_Change_ComboBox(self, event):
        select = self.txtVariableOpc.get()
        for i in range(len(self.Cajeros)):
            if self.Cajeros[i].Sucursal == select:
                self.selecCajero = i
        if(select == "Agregar Cajero"):
            top = AñadirCajero(self, self.Cajeros)
            top.protocol("WM_DELETE_WINDOW", lambda: self.on_toplevel_close(top))

        print(self.selecCajero)
    
    def on_toplevel_close(self, top: Toplevel):
        self.listaCajeros = []
        for cajero in self.Cajeros:
            self.listaCajeros.append(cajero.Sucursal)
        self.listaCajeros.append("Agregar Cajero")
        self.CmbCajeros['values'] = self.listaCajeros
        top.destroy()

def Main():
    app = MainPanel()
    app.mainloop()


Main()

# py_hot_reload.run_with_reloader(Main)

