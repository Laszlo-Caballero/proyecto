from tkinter import Toplevel, Label, Frame, Entry, StringVar, Button, ttk, END, messagebox
import pickle
from Class.Cajero import Cajero
from Class.Billete import Billete

class InterfazActualizarDepostio(Toplevel):
    def __init__(self, parent, cajero):
        super().__init__(parent)
        self.title("Actulizar Depostio")
        self.geometry("500x200")

        self.IdxCajero = cajero
        self.IdxBilelte = -1
        with open('Data/Cajero.pkl', 'rb') as file:
            self.LstCajero : list[Cajero] = pickle.load(file)
        self.Cajero = self.LstCajero[self.IdxCajero]
        

        self.lbl = Label(self, text=f"Actualizar Deposito de la sucursal {self.Cajero.Sucursal}")
        self.lbl.pack()

        self.FramePrincipal = Frame(self)
        
        self.txtVDinero = StringVar()
        self.txtVDinero.set(f"Dinero Del cajero: {self.Cajero.DineroCajero}") 
        
        self.lblDinero = Label(self, textvariable=self.txtVDinero)
        self.lblDinero.pack()

        self.FrameEstado = Frame(self.FramePrincipal)

        self.txtEstadoActual = StringVar()
        self.txtEstadoActual.set(f"El Estado Actual es: {self.Cajero.Estado}")
        self.lblEstado = Label(self.FrameEstado, textvariable=self.txtEstadoActual)
        self.lblEstado.pack()

        self.txtcmbEstado = StringVar()
        self.cmbEstado = ttk.Combobox(self.FrameEstado, textvariable=self.txtcmbEstado, state='readonly')
        self.cmbEstado['values'] = ("A", "M", "N")
        self.cmbEstado.bind("<<ComboboxSelected>>", self.on_change_comboBoxEstado)
        self.cmbEstado.pack()


        self.FrameEstado.pack(side='left')

        self.FrameBilletes = Frame(self.FramePrincipal)

        self.lblBilletes = Label(self.FrameBilletes, text="Billetes a Añadir")
        self.lblBilletes.pack()

        self.txtComboBox = StringVar()
        self.ComboBoxBilletes = ttk.Combobox(self.FrameBilletes, textvariable=self.txtComboBox, state='readonly')
        self.ComboBoxBilletes['values'] = ("200", "100", "50", "20", "10")
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

        self.FrameBilletes.pack(side='right', anchor="w")

        self.FramePrincipal.pack(expand=True)
    
    def on_change_comboBox(self, event):
        billete = int(self.txtComboBox.get())
        print(billete)
        for i in range(len(self.Cajero.Billetes)):
            if self.Cajero.Billetes[i].Valor == billete:
                self.txtvariable.set(f"Cantidad de billetes: {self.Cajero.Billetes[i].Cantidad}")
                print(self.Cajero.Billetes[i].Cantidad)
                self.IdxBilelte = i
                break
    
    def on_change_comboBoxEstado(self, event):
         estado = self.cmbEstado.get()
         self.txtcmbEstado.set(estado)
         self.Cajero.Estado = estado
         self.txtEstadoActual.set(f"El Estado Actual es: {self.Cajero.Estado}")
         Cajero.Guardar(self.LstCajero)
         


    def AñadirBillete(self):
        if self.IdxBilelte != -1:
                billete = int(self.txtComboBox.get())
                cantidad = int(self.txtCantidad.get())
                self.Cajero.AñadirDinero(Billete(billete, cantidad))
                self.txtVDinero.set(f"Dinero Del cajero: {self.Cajero.DineroCajero}")
                self.txtvariable.set(f"Cantidad de billetes: {self.Cajero.Billetes[self.IdxBilelte].Cantidad}") 
                Cajero.Guardar(self.LstCajero)
        else:
             messagebox.showerror("Error", "Elija Un billete a insertar")

