from tkinter import Toplevel, Frame, ttk, Label, Button
from PIL import Image, ImageTk
from Class.Font import Font
from Components.Boton import Boton

class Retirar(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Retirar Dinero")
        self.geometry("900x500")
        

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
        self.txtMonto = ttk.Entry(self.FrameEntry, width=30)
        self.txtMonto.grid(row=1, column=0, pady=(5, 10), ipady=8)
        self.btnConfirmar = Boton(self.FrameEntry, "Confirmar")
        self.btnConfirmar.config(width=20)
        self.btnConfirmar.grid(row=2, column=0, ipady=15)
        self.FrameEntry.grid(row=0, column=0)


        self.FrameBtn = Frame(self.FramePrincipal)
        
        style = ttk.Style()
        style.configure('Blue-Font', borderwidth=0, relief="flat", bordercolor="#000000", foreground='Blue')
        Dinero = ["20", "50", "100", "200"]
        for btn in range(len(Dinero)):
            boton = Boton(self.FrameBtn, Dinero[btn])
            boton.grid(row=btn//2, column=btn%2, padx=5, pady=10, ipadx=20, ipady=20)

        self.FrameBtn.grid(row=0, column=1)
        self.FramePrincipal.pack(expand=True)


        self.FrameFooter = Frame(self)


        self.lbl4 = Label(self.FrameFooter, text="21023")
        self.lbl4.pack()


        self.FrameFooter.pack(expand=True)