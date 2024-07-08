from tkinter import Toplevel, Label, Frame, StringVar, Entry, CENTER, Button
from Class.Font import Font
from Class.Usuario import Usuario
from Components.Mensaje import Mensaje

class InterfazEditar(Toplevel):
    def __init__(self, parent, usuario: Usuario):
        super().__init__(parent)
        self.Usuario = usuario
        self.title(f"Editar Usuario de {self.Usuario.nombre}")
        self.geometry("400x300")
        
        self.lbl1 = Label(self, text="Editar Usuario", font=Font(self, 18, "Bold").Font, foreground="#1f348d")
        self.lbl1.pack(pady=(10,0))

        self.FrameInptNombre = Frame(self)

        self.lbl2 = Label(self.FrameInptNombre, text="Nombre", font=Font(self, 12, "Bold").Font, foreground="#1f348d")
        self.lbl2.pack(side="left", padx=10)

        self.strNombre = StringVar()
        self.strNombre.set(self.Usuario.nombre)
        self.txtNombre = Entry(self.FrameInptNombre, textvariable=self.strNombre)
        self.txtNombre.pack()

        self.FrameInptNombre.pack(pady=20)


        self.FrameNumeroCuenta = Frame(self)

        self.lbl3 = Label(self.FrameNumeroCuenta, text="Numero de cuenta", font=Font(self, 12, "Bold").Font, foreground="#1f348d")
        self.lbl3.pack(side="left", padx=10)
        
        self.strNumeroCuenta = StringVar()
        self.strNumeroCuenta.set(self.Usuario.numeroCuenta)
        self.txtNumeroCuenta = Entry(self.FrameNumeroCuenta, textvariable=self.strNumeroCuenta)
        self.txtNumeroCuenta.pack()

        self.FrameNumeroCuenta.pack()

        self.FrameContraseña = Frame(self)

        self.lbl4 = Label(self.FrameContraseña, text="Contraseña", font=Font(self, 12, "Bold").Font, foreground="#1f348d")
        self.lbl4.pack(side="left", padx=10)

        self.strContraseña = StringVar()
        self.strContraseña.set(self.Usuario.contraseña)
        self.txtContraseña = Entry(self.FrameContraseña, textvariable=self.strContraseña)
        self.txtContraseña.pack()

        self.FrameContraseña.pack(pady=20)


        self.btnAct = Button(self, text="Actualizar", fg="white", bg="#F36F2C", borderwidth=0, relief="flat", width=15, command=self.Actualizar)

        self.btnAct.pack()

    def Actualizar(self):
        nombre = self.strNombre.get()
        numeroCuenta = self.strNumeroCuenta.get()
        contraseña = self.strContraseña.get()
        self.Usuario.nombre = nombre
        self.Usuario.numeroCuenta = numeroCuenta
        self.Usuario.contraseña = contraseña

        Mensaje(self, tipo='Check', mensaje="Se Actualizo correctamente")

        