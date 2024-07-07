from tkinter import Toplevel, Label, Frame, Entry, Button
from Class.Cajero import Cajero

class AñadirCajero(Toplevel):
    def __init__(self, parent, datos):
        super().__init__(parent)
        self.title("Añadir Cajero")
        self.geometry("400x300")
        self.config(bg="white")
        self.Cajeros : list[Cajero] = datos
        
        self.FramePrincipal = Frame(self, bg='white')
        self.FramePrincipal.pack(expand=True)
        self.lbl1 =  Label(self.FramePrincipal, text="Añadir Cajero", bg='white')
        self.lbl1.pack()

        self.lbl2 = Label(self.FramePrincipal, text="Nombre de la sucursual donde esta el cajero", bg='white')
        self.lbl2.pack()

        self.txtNombre = Entry(self.FramePrincipal)
        self.txtNombre.pack()

        self.btnAñadir = Button(self.FramePrincipal, text="Añadir", command=self.Añadir)
        self.btnAñadir.pack()


    def Añadir(self):
        nuevo = Cajero(self.txtNombre.get())
        self.Cajeros.append(nuevo)
        Cajero.Guardar(self.Cajeros)