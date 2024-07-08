from tkinter import Toplevel, Label, Frame, Entry, StringVar, Button, messagebox
from tkinter import ttk
from Components.Mensaje import Mensaje

class InterfazServicios(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Servicios")
        self.geometry("500x350")

        azul_oscuro = "#1D4E8F"
        azul_claro = "#4182C4"
        naranja = "#F28C28"

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
        self.cmbServicio['values'] = ["Agua", "Luz"]
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
        codigo_pago = self.txtCodigo.get()
        monto = self.txtMonto.get()
        if not servicio or not codigo_pago or not monto:
            Mensaje(self, tipo='Error', mensaje= "Por favor, ingrese todos los campos")
        else:
            try:
                monto = float(monto)
                if monto <= 0:
                    raise ValueError
                Mensaje(self, tipo='Check', mensaje= f"Se ha pagado {monto} al servicio {servicio} con el código {codigo_pago}")
                
                
            except ValueError:
                Mensaje(self, tipo='Check', mensaje= "Por favor, ingrese un monto válido")


if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    root.withdraw()  
    app = InterfazServicios(root)
    app.mainloop()
