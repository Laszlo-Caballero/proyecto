from tkinter import Toplevel, Label, Frame, Entry, StringVar, Button, messagebox
from Class.Usuario import Usuario
from Class.Cajero import Cajero
from Components.Mensaje import Mensaje
import pickle


class InterfazTransferencia(Toplevel):
    def __init__(self, parent, usuario: Usuario):
        super().__init__(parent)
        self.title("Transferencia de Dinero")
        self.geometry("500x300")


        self.Usuario = usuario
        with open(r"Data/Usuario.pkl", 'rb') as file:
            self.Usuarios: list[Usuario] = pickle.load(file) 
        
        self.IdxUsuario = -1

        for i in range(len(self.Usuarios)):
            if self.Usuarios[i].numeroCuenta == self.Usuario.numeroCuenta:
                self.IdxUsuario = i

        azul_oscuro = "#1D4E8F"
        azul_claro = "#4182C4"
        naranja = "#F28C28"

        self.lbl = Label(self, text="Transferencia de Dinero", font=("Arial", 14), fg=azul_oscuro)
        self.lbl.pack(pady=10, anchor="w")

        # Frame principal
        self.FramePrincipal = Frame(self)
        self.FramePrincipal.pack(expand=True, pady=10, padx=10)

        # Frame del número de cuenta
        self.FrameCuenta = Frame(self.FramePrincipal)
        self.FrameCuenta.pack(pady=10)

        self.lblCuenta = Label(self.FrameCuenta, text="Número de cuenta:", font=("Arial", 12), fg=azul_claro)
        self.lblCuenta.pack(side='left', padx=10)

        self.txtCuenta = Entry(self.FrameCuenta, font=("Arial", 12))
        self.txtCuenta.pack(side='left', padx=10)

        # Frame del monto 
        self.FrameMonto = Frame(self.FramePrincipal)
        self.FrameMonto.pack(pady=10)

        self.lblMonto = Label(self.FrameMonto, text="Monto a transferir:", font=("Arial", 12), fg=azul_claro)
        self.lblMonto.pack(side='left', padx=10)

        self.txtMonto = Entry(self.FrameMonto, font=("Arial", 12))
        self.txtMonto.pack(side='left', padx=10)

        # Botón transferencia
        self.btnTransferir = Button(self.FramePrincipal, text="Realizar Transferencia", command=self.realizar_transferencia, font=("Arial", 12), bg=naranja, fg="white")
        self.btnTransferir.pack(pady=20)

    def realizar_transferencia(self):
        try:
            numero_cuenta = self.txtCuenta.get()
            monto = int(self.txtMonto.get())
            receptor = -1
            for i in range(len(self.Usuarios)):
                if self.Usuarios[i].numeroCuenta == numero_cuenta:
                    receptor = i
                    break
            if receptor != -1 and receptor != self.IdxUsuario:
                error = Cajero.Transferencia(int(monto), self.Usuarios[self.IdxUsuario], self.Usuarios[receptor])

                if error != "" : 
                    Mensaje(self, tipo='Error', mensaje= error)
                else:
                    Usuario.Guardar(self.Usuarios)
                    Mensaje(self, tipo='Check', mensaje= "Se completo la transferencia")
            else:
                Mensaje(self, tipo='Error', mensaje= "No se encontro el numero de cuenta o numero de cuenta no valido")
                
        except:
            Mensaje(self, tipo='Error', mensaje= "No ingreso datos validos")
            


