from tkinter import Toplevel, Frame, ttk, Label, CENTER
from PIL import Image, ImageTk
from Class.Usuario import Usuario
from Class.Cajero import Cajero
from Class.Font import Font
from Components.Deposito import CDinero
from Components.Boton import Boton
from Class.Billete import Billete
import pickle


class InterfazDepositar(Toplevel):
    def __init__(self, parent, usuario: Usuario, cajero: Cajero = None):
        super().__init__(parent)
        self.title("Depositar")
        self.geometry("900x500")
        self.Usuario = usuario
        self.Cajero = cajero
        with open(r'Data/Cajero.pkl', 'rb') as file:
            self.Cajeros : list[Cajero] = pickle.load(file)
        with open(r"Data/Usuario.pkl", 'rb') as file:
            self.Usuarios: list[Usuario] = pickle.load(file) 
        
        self.IdxUsuario = -1
        self.selecCajero = -1

        for i in range(len(self.Cajeros)):
            if self.Cajeros[i].Sucursal == self.Cajero.Sucursal:
                self.selecCajero = i
                break
        for i in range(len(self.Usuarios)):
            if self.Usuarios[i].numeroCuenta == self.Usuario.numeroCuenta:
                self.IdxUsuario = i

        self.Font = Font(self, 12, Font="Bold").Font
        self.Font2 = Font(self, 15, Font="Bold").Font
        self.FrameHeader = Frame(self)

        iconIngresar = Image.open("./images/ingresar.png")
        self.iconIngresar = ImageTk.PhotoImage(iconIngresar)
        self.lblIconIngresar = ttk.Label(self.FrameHeader, image=self.iconIngresar)

        self.lblIconIngresar.grid(row=0, column=0, padx=(10,0))


        self.FrameTxt = Frame(self.FrameHeader)


        self.lbl1 = Label(self.FrameTxt, text="Depositar Efectivo", font=self.Font)
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2 = Label(self.FrameTxt, text="Ingrese el monto a Depositar", font=self.Font2)
        self.lbl2.grid(row=1, column=0)

        self.FrameTxt.grid(row=0, column=1)

        self.FrameHeader.pack(fill='both')


        self.FramePrincipal = Frame(self)

        self.inputs : list[CDinero] = []
        
        billetes = ["200", "100", "50", "20", "10"]

        for i in range(len(billetes)):
            inputNumber = CDinero(self.FramePrincipal, billetes[i])
            inputNumber.grid(row=i//2, column=i%2)
            self.inputs.append(inputNumber)

        self.FramePrincipal.pack(expand=True)

        self.btnDepositar = Boton(self, "Depositar", position=CENTER, command=self.Depostiar)
        self.btnDepositar.pack(side="bottom", pady=(0, 30))


    def Depostiar(self):
        monto = 0
        lista_Billetes : list[Billete] = []
        for ipt in self.inputs:
            monto += int(ipt.get_Cantidad()) * int(ipt.valor)
            if ipt.get_Cantidad() != "0":
                billete = Billete(int(ipt.valor), int(ipt.get_Cantidad()))
                lista_Billetes.append(billete)


        


        