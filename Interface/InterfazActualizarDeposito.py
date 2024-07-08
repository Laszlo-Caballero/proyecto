from tkinter import Toplevel, Label, Frame, Entry, StringVar, Button, ttk, messagebox
import pickle
from Class.Cajero import Cajero
from Class.Billete import Billete

class InterfazActualizarDeposito(Toplevel):
    def __init__(self, parent, cajero):
        super().__init__(parent)
        self.title("Actualizar Depósito")
        self.geometry("500x300")

        self.IdxCajero = cajero
        self.IdxBillete = -1
        with open('Data/Cajero.pkl', 'rb') as file:
            self.LstCajero: list[Cajero] = pickle.load(file)
        self.Cajero = self.LstCajero[self.IdxCajero]

        # Título
        self.lbl = Label(self, text=f"Actualizar depósito de la sucursal {self.Cajero.Sucursal}", font=("Arial", 14))
        self.lbl.pack(pady=10)

        # Subtítulo
        self.txtVDinero = StringVar()
        self.txtVDinero.set(f"Dinero del cajero: {self.Cajero.DineroCajero}")
        self.lblDinero = Label(self, textvariable=self.txtVDinero, font=("Arial", 12))
        self.lblDinero.pack(pady=5)

        # Frame principal
        self.FramePrincipal = Frame(self)
        self.FramePrincipal.pack(expand=True, pady=10, padx=10)

        # Frame del estado
        self.FrameEstado = Frame(self.FramePrincipal)
        self.FrameEstado.pack(side='left', padx=20, pady=10)

        self.txtEstadoActual = StringVar()
        self.txtEstadoActual.set(f"El estado actual es: {self.Cajero.Estado}")
        self.lblEstado = Label(self.FrameEstado, textvariable=self.txtEstadoActual, font=("Arial", 12))
        self.lblEstado.pack(pady=5)

        self.txtcmbEstado = StringVar()
        self.cmbEstado = ttk.Combobox(self.FrameEstado, textvariable=self.txtcmbEstado, state='readonly', font=("Arial", 12))
        self.cmbEstado['values'] = ("A", "M", "N")
        self.cmbEstado.bind("<<ComboboxSelected>>", self.on_change_comboBoxEstado)
        self.cmbEstado.pack(pady=5)

        # Frame de los billetes
        self.FrameBilletes = Frame(self.FramePrincipal)
        self.FrameBilletes.pack(side='right', padx=20, pady=10)

        self.lblBilletes = Label(self.FrameBilletes, text="Billetes a añadir", font=("Arial", 12))
        self.lblBilletes.pack(pady=5)

        self.txtComboBox = StringVar()
        self.ComboBoxBilletes = ttk.Combobox(self.FrameBilletes, textvariable=self.txtComboBox, state='readonly', font=("Arial", 12))
        self.ComboBoxBilletes['values'] = ("200", "100", "50", "20")
        self.ComboBoxBilletes.bind("<<ComboboxSelected>>", self.on_change_comboBox)
        self.ComboBoxBilletes.pack(pady=5)

        # Frame para la cantidad de billetes
        self.FrameCantidad = Frame(self)
        self.FrameCantidad.pack(pady=10)

        self.txtvariable = StringVar()
        self.txtvariable.set("Cantidad de billetes:")
        self.lblBillete = Label(self.FrameCantidad, textvariable=self.txtvariable, font=("Arial", 12))
        self.lblBillete.pack(pady=5)

        self.txtCantidad = Entry(self.FrameCantidad, font=("Arial", 12))
        self.txtCantidad.pack(pady=5)

        self.btnAñadirBilletes = Button(self.FrameCantidad, text="Añadir Billetes", command=self.AñadirBillete, font=("Arial", 12))
        self.btnAñadirBilletes.pack(pady=10)

    def on_change_comboBox(self, event):
        billete = int(self.txtComboBox.get())
        for i in range(len(self.Cajero.Billetes)):
            if self.Cajero.Billetes[i].Valor == billete:
                self.txtvariable.set(f"Cantidad de billetes: {self.Cajero.Billetes[i].Cantidad}")
                self.IdxBillete = i
                break

    def on_change_comboBoxEstado(self, event):
        estado = self.cmbEstado.get()
        self.txtcmbEstado.set(estado)
        self.Cajero.Estado = estado
        self.txtEstadoActual.set(f"El Estado Actual es: {self.Cajero.Estado}")
        Cajero.Guardar(self.LstCajero)

    def AñadirBillete(self):
        if self.IdxBillete != -1:
            billete = int(self.txtComboBox.get())
            cantidad = int(self.txtCantidad.get())
            self.Cajero.AñadirDinero(Billete(billete, cantidad))
            self.txtVDinero.set(f"Dinero del cajero: {self.Cajero.DineroCajero}")
            self.txtvariable.set(f"Cantidad de billetes: {self.Cajero.Billetes[self.IdxBillete].Cantidad}")
            Cajero.Guardar(self.LstCajero)
        else:
            messagebox.showerror("Error", "Elija un billete a insertar")

