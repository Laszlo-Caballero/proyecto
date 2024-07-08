from tkinter import Toplevel, Frame, ttk, Label, Button, StringVar, LEFT, CENTER, messagebox
from PIL import Image, ImageTk
import pickle
from Class.Usuario import Usuario
from Class.Font import Font
from Class.Cajero import Cajero
from Components.Boton import Boton
from Components.Mensaje import Mensaje
from Class.Billete import Billete

class Retirar(Toplevel):
    def __init__(self, parent, usuario: Usuario, cajero: Cajero = None):
        super().__init__(parent)
        self.title("Retirar Dinero")
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


        self.FrameHeader = Frame(self, width=900, height=70)
        
        self.Font = Font(self, 12, Font="Bold").Font
        self.Font2 = Font(self, 15, Font="Bold").Font
        
        iconRetiro = Image.open("./images/retiro2.png")
        self.iconRetiro = ImageTk.PhotoImage(iconRetiro)
        self.lblIconRetiro = ttk.Label(self.FrameHeader, image=self.iconRetiro)
        self.lblIconRetiro.grid(row=0, column=0, padx=(10,0))


        self.FrameTxt = Frame(self.FrameHeader)


        self.lbl1 = Label(self.FrameTxt, text="Retiro de Efectivo", font=self.Font)
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2 = Label(self.FrameTxt, text="Ingresa o Selecciona el monto a retirar", font=self.Font2)
        self.lbl2.grid(row=1, column=0)

        self.FrameTxt.grid(row=0, column=1)

        self.FrameHeader.pack()
        self.FrameHeader.grid_propagate(False)


        self.FramePrincipal = Frame(self)

        self.FrameEntry = Frame(self.FramePrincipal)
        self.lbl3 = Label(self.FrameEntry, text="Ingresar Monto", font=Font(self, 15, Font="Bold").Font)
        self.lbl3.grid(row=0, column=0, sticky='w')

        self.strMonto = StringVar()
        self.strMonto.set("0")
        self.txtMonto = ttk.Entry(self.FrameEntry, width=30, textvariable=self.strMonto, state='readonly')
        self.txtMonto.grid(row=1, column=0, pady=(5, 10), ipady=8)
        self.btnConfirmar = Boton(self.FrameEntry, "Confirmar", command=self.Retirar)
        self.btnConfirmar.config(width=20)
        self.btnConfirmar.grid(row=2, column=0, ipady=15)
        self.FrameEntry.grid(row=0, column=0)


        self.FrameBtn = Frame(self.FramePrincipal)
        
        style = ttk.Style()
        style.configure('Blue-Font', borderwidth=0, relief="flat", bordercolor="#000000", foreground='Blue')
        Dinero = ["10","20", "50", "100", "200", ""]
        Img = ["","","","","","images/borrar.png"]
        for btn in range(len(Dinero)):
            if btn != 5:
                boton = Boton(self.FrameBtn, Dinero[btn],Img[btn], command=lambda b=Dinero[btn]: self.AñadirDinero(b))
                boton.grid(row=btn//2, column=btn%2, padx=5, pady=10, ipadx=20, ipady=20)
            else:
                boton = Boton(self.FrameBtn, Dinero[btn],Img[btn], command=lambda b=Dinero[btn]: self.AñadirDinero(b), position=CENTER)
                boton.grid(row=btn//2, column=btn%2, padx=5, pady=10, ipadx=20, ipady=14)

        self.FrameBtn.grid(row=0, column=1)
        self.FramePrincipal.pack(expand=True)


        self.FrameFooter = Frame(self)
        

        self.FrameTxtFooter = Frame(self.FrameFooter)

        self.lbl4 = Label(self.FrameTxtFooter, text="Cuenta:")
        self.lbl4.grid(row=0, column=0, sticky='w')
        self.lbl5 = Label(self.FrameTxtFooter, text="Ahorro en soles S/")
        self.lbl5.grid(row=1, column=0, padx=(0,50))


        self.lbl6 = Label(self.FrameTxtFooter, text="Saldo Disponible")
        self.lbl6.grid(row=0, column=1)

        self.txtVariable = StringVar()
        self.txtVariable.set("******")
        self.lblSaldo = ttk.Label(self.FrameTxtFooter, textvariable=self.txtVariable)
        self.lblSaldo.grid(row=1, column=1, sticky='w')

        self.FrameTxtFooter.grid(row=0, column=0, padx=(0,50))

        self.btnVerSaldo = Boton(self.FrameFooter, text="Ver Saldo", image_path="images/ojo.png", position=LEFT, command=self.Ver_Saldo)
        self.btnVerSaldo.grid(row=0, column=1)

        

        self.FrameFooter.pack(expand=True)
    
    def Ver_Saldo(self):
        if (self.txtVariable.get() == "******"):
            self.txtVariable.set(self.Usuario.dinero)
        else:
            self.txtVariable.set("******")

    def AñadirDinero(self, texto):
        if texto and texto != "":
            txtEntry = int(self.strMonto.get()) + int(texto)
            self.strMonto.set(str(txtEntry))
        elif int(self.strMonto.get()) >=10:
            txtEntry = int(self.strMonto.get()) - 10
            self.strMonto.set(str(txtEntry))

    def Retirar(self):
        dinero = self.txtMonto.get()
        if dinero != "0":
            error, lista = self.Cajeros[self.selecCajero].RetirarDinero(int(dinero), self.Usuarios[self.IdxUsuario])
            if error == "":
                Cajero.Guardar(self.Cajeros)
                Usuario.Guardar(self.Usuarios)
                CantBilletes = "Se Completo el retiro \n"
                for billetes in lista:
                    CantBilletes += f"Se Desgloso {billetes.Cantidad} Billete de {billetes.Valor} \n"
                Mensaje(self, tipo='Check', mensaje= CantBilletes)
            else:
                Mensaje(self, tipo='Error', mensaje= error)