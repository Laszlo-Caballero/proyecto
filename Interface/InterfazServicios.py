from tkinter import Toplevel, Label, Frame, Entry, StringVar, Button, messagebox
from tkinter import ttk
from Components.Mensaje import Mensaje
from Class.Usuario import Usuario
from Class.Movimiento import Movimiento
import pickle

class InterfazServicios(Toplevel):
    def __init__(self, parent, usuario: Usuario):
        super().__init__(parent)
        self.title("Servicios")
        self.geometry("500x350")

        azul_oscuro = "#1D4E8F"
        azul_claro = "#4182C4"
        naranja = "#F28C28"

        self.Usuario = usuario
        with open(r"Data/Usuario.pkl", 'rb') as file:
            self.Usuarios: list[Usuario] = pickle.load(file) 
        
        self.IdxUsuario = -1

        for i in range(len(self.Usuarios)):
            if self.Usuarios[i].numeroCuenta == self.Usuario.numeroCuenta:
                self.IdxUsuario = i

        self.lbl = Label(self, text="Servicios", font=("Arial", 14), fg=azul_oscuro)
        self.lbl.pack(pady=10, anchor="w")

        # Frame principal
        self.FramePrincipal = Frame(self)
        self.FramePrincipal.pack(expand=True, pady=10, padx=10)

        # Frame del servicio a pagar
        self.FrameServicio = Frame(self.FramePrincipal)
        self.FrameServicio.pack(pady=10)

        self.lblServicio = Label(self.FrameServicio, text="Servicio a pagar:", font=("Arial", 12), fg=azul_claro)
        self.lblServicio.pack(side='left', padx=10)

        self.servicio_var = StringVar()
        self.cmbServicio = ttk.Combobox(self.FrameServicio, textvariable=self.servicio_var, state='readonly')
        self.cmbServicio['values'] = ["Agua", "Luz", "Internet", "Otros"]
        self.cmbServicio.current(0)  
        self.cmbServicio.pack(side='left', padx=10)

        self.FrameCodigo = Frame(self.FramePrincipal)
        self.FrameCodigo.pack(pady=10)

        self.lblCodigo = Label(self.FrameCodigo, text="Código de pago:", font=("Arial", 12), fg=azul_claro)
        self.lblCodigo.pack(side='left', padx=10)

        self.txtCodigo = Entry(self.FrameCodigo, font=("Arial", 12))
        self.txtCodigo.pack(side='left', padx=10)

        # Frame del monto 
        self.FrameMonto = Frame(self.FramePrincipal)
        self.FrameMonto.pack(pady=10)

        self.lblMonto = Label(self.FrameMonto, text="Monto a transferir:", font=("Arial", 12), fg=azul_claro)
        self.lblMonto.pack(side='left', padx=10)

        self.txtMonto = Entry(self.FrameMonto, font=("Arial", 12))
        self.txtMonto.pack(side='left', padx=10)

        # Botón realizar pago
        self.btnPagar = Button(self.FramePrincipal, text="Realizar Pago", command=self.realizar_pago, font=("Arial", 12), bg=naranja, fg="white")
        self.btnPagar.pack(pady=20)

    def realizar_pago(self):
        servicio = self.servicio_var.get()

        try:
            codigo_pago = int(self.txtCodigo.get())
            monto = int(self.txtMonto.get())

            if monto <= self.Usuarios[self.IdxUsuario].dinero:
                self.Usuarios[self.IdxUsuario].dinero -= monto
                self.Usuarios[self.IdxUsuario].movimientos.append(Movimiento(self.Usuario.numeroCuenta, f"Servicio {servicio}", monto, f"P {servicio} {codigo_pago}"))
                Mensaje(self, tipo='Check', mensaje="Se pago correctamente el Servicio")
                Usuario.Guardar(self.Usuarios)

            else:
                Mensaje(self, tipo='Error', mensaje="No tiene le suficiente dinero para pagar el servicio")


        except:
            Mensaje(self, tipo='Error', mensaje="Ingrese los datos Correctos")
