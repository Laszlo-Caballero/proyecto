from tkinter import Toplevel, Label, Frame, Entry, StringVar, Button, messagebox

class InterfazTransferencia(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Transferencia de Dinero")
        self.geometry("500x300")

        # Título
        self.lbl = Label(self, text="Transferencia de Dinero", font=("Arial", 14))
        self.lbl.pack(pady=10)

        # Frame principal
        self.FramePrincipal = Frame(self)
        self.FramePrincipal.pack(expand=True, pady=10, padx=10)

        # Frame del número de cuenta
        self.FrameCuenta = Frame(self.FramePrincipal)
        self.FrameCuenta.pack(pady=10)

        self.lblCuenta = Label(self.FrameCuenta, text="Número de cuenta:", font=("Arial", 12))
        self.lblCuenta.pack(side='left', padx=10)

        self.txtCuenta = Entry(self.FrameCuenta, font=("Arial", 12))
        self.txtCuenta.pack(side='left', padx=10)

        # Frame del monto 
        self.FrameMonto = Frame(self.FramePrincipal)
        self.FrameMonto.pack(pady=10)

        self.lblMonto = Label(self.FrameMonto, text="Monto a transferir:", font=("Arial", 12))
        self.lblMonto.pack(side='left', padx=10)

        self.txtMonto = Entry(self.FrameMonto, font=("Arial", 12))
        self.txtMonto.pack(side='left', padx=10)

        # Botón transferencia
        self.btnTransferir = Button(self.FramePrincipal, text="Realizar Transferencia", command=self.realizar_transferencia, font=("Arial", 12))
        self.btnTransferir.pack(pady=20)

    def realizar_transferencia(self):
        numero_cuenta = self.txtCuenta.get()
        monto = self.txtMonto.get()
        if not numero_cuenta or not monto:
            messagebox.showerror("Error", "Por favor, ingrese todos los campos")
        else:
            try:
                monto = float(monto)
                if monto <= 0:
                    raise ValueError
                messagebox.showinfo("Éxito", f"Se ha transferido {monto} a la cuenta {numero_cuenta}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un monto válido")


if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    root.withdraw()  
    app = InterfazTransferencia(root)
    app.mainloop()
