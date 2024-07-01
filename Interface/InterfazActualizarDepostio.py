from tkinter import Toplevel, Label, Frame, Entry, StringVar, Button, ttk, END
import pickle
from Class.Cajero import Cajero
from Class.Billete import Billete

class InterfazActualizar(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Actulizar Depostio")
        self.geometry("500x200")
        self.lbl = Label(self, text="Actualizar Deposito")
        self.lbl.pack()
        with open('Data/Cajero.pkl', 'rb') as file:
            self.Cajero : Cajero = pickle.load(file)
        
        self.FramePrincipal = Frame(self)
        
        self.FrameDinero = Frame(self.FramePrincipal)
        
        self.txtVDinero = StringVar()
        self.txtVDinero.set(f"Dinero Del cajero: {self.Cajero.DineroCajero}") 
        
        self.lblDinero = Label(self.FrameDinero, textvariable=self.txtVDinero)
        self.lblDinero.pack()
    
        self.lbl1 = Label(self.FrameDinero, text="Cantidad a Añadir")
        self.lbl1.pack(pady=(10,0))
        
        self.txtDinero = Entry(self.FrameDinero)
        self.txtDinero.pack(pady=(0, 10))
        
        self.btnAñadir = Button(self.FrameDinero, text="Añadir Dinero")
        self.btnAñadir.pack()
        self.FrameDinero.pack(side='left', padx=(0,100))

        self.FrameBilletes = Frame(self.FramePrincipal)

        self.lblBilletes = Label(self.FrameBilletes, text="Billetes a Añadir")
        self.lblBilletes.pack()

        self.txtComboBox = StringVar()
        self.ComboBoxBilletes = ttk.Combobox(self.FrameBilletes, textvariable=self.txtComboBox, state='readonly')
        self.ComboBoxBilletes['values'] = ("200", "100", "50", "20")
        self.ComboBoxBilletes.bind("<<ComboboxSelected>>", self.on_change_comboBox)

        self.ComboBoxBilletes.pack()

        self.txtvariable = StringVar()
        self.txtvariable.set(f"Cantidad de billetes: ")
        self.lblBillete = Label(self.FrameBilletes, textvariable=self.txtvariable)
        self.lblBillete.pack(pady=(10,0))

        self.txtCantidad = Entry(self.FrameBilletes)
        self.txtCantidad.pack()

        self.btnAñadirBileltes = Button(self.FrameBilletes, text="Añadir Billetes", command=self.AñadirBillete)
        self.btnAñadirBileltes.pack(pady=(10,0))

        self.FrameBilletes.pack(side='right')

        self.FramePrincipal.pack(expand=True)
    
    def on_change_comboBox(self, event):
        billete = int(self.txtComboBox.get())
        print(billete)
        for i in range(len(self.Cajero.Billetes)):
            if self.Cajero.Billetes[i].Valor == billete:
                self.txtvariable.set(f"Cantidad de billetes: {self.Cajero.Billetes[i].Cantidad}")
                print(self.Cajero.Billetes[i].Cantidad)
                break

    def AñadirBillete(self):
        billete = int(self.txtComboBox.get())
        for i in range(len(self.Cajero.Billetes)):
            if self.Cajero.Billetes[i].Valor == billete:
                self.Cajero.Billetes[i].Cantidad += int(self.txtCantidad.get())
                self.txtvariable.set(f"Cantidad de billetes: {self.Cajero.Billetes[i].Cantidad}")
                self.txtCantidad.delete(0, END)
                break
        self.Cajero.Guardar()
    def AñadirDinero(self):
        pass