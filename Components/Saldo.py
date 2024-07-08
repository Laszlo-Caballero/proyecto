from tkinter import *
from tkinter import font
from PIL import Image, ImageTk, ImageFont


class Saldo(Frame):
    def __init__(self, root, NumCuenta, Saldo, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.TipoCuenta = "Ahorro Soles"
        self.NumeroCuenta = NumCuenta
        self.Saldo = Saldo
        ##Font
        self.LoadCustomRegular = ImageFont.truetype("./font/Flexo-Regular-webfont.ttf", size=12)
        self.LoadCustomBold = ImageFont.truetype("./font/Flexo-Bold-webfont.ttf", size=12)
        self.LoadCustomDemi = ImageFont.truetype("./font/Flexo-Demi-webfont.ttf", size=12)
        self.FontRegular = font.Font(self, family=self.LoadCustomRegular.font, size=12, weight="normal")
        self.FontDisponbleRegular = font.Font(self, family=self.LoadCustomRegular.font, size=8, weight="normal")
        self.FontSaldoRegular = font.Font(self, family=self.LoadCustomRegular.font, size=9, weight="normal")  
        self.FontBold = font.Font(self, family=self.LoadCustomBold.font, size=10, weight="bold")
        self.FontDmi = font.Font(self, family=self.LoadCustomDemi.font, size=12, weight="bold")
        #Header
        self.CointainerHeader = Frame(self)
        self.CointainerHeader.config(bg="white")
        self.LblProductos = Label(self.CointainerHeader, text="Mis Productos", bg="white", font=self.FontRegular, fg="#1f348d")
        self.LblProductos.grid(row=1, column=1, padx=(0, 330))
        self.ImageOjoPil = Image.open("./images/ojo.png").resize((20, 20))
        self.ImgOjo = ImageTk.PhotoImage(image=self.ImageOjoPil)
        self.btnOjo = Button(self.CointainerHeader, image=self.ImgOjo, bg="white")
        self.imgConfigPil = Image.open("./images/ajuste.png").resize((20,20))
        self.ImgConfig = ImageTk.PhotoImage(image=self.imgConfigPil)
        self.btnConfig = Button(self.CointainerHeader, image=self.ImgConfig, bg="white")
        self.btnOjo.config(borderwidth=0, highlightthickness=0)
        self.btnConfig.config(borderwidth=0, highlightthickness=0)
        self.btnOjo.grid(row=1, column=2, padx=(0,30))
        self.btnConfig.grid(row=1, column=3)
        self.CointainerHeader.pack()
        #Cuenta
        self.ConteinerCuenta = Frame(self, bg="white")
        #Imagen Cuenta
        self.CointainerImgCuenta = Frame(self.ConteinerCuenta, bg="white")
        self.ImgPil = Image.open("./images/cosa.png").resize((50, 60))
        self.Img = ImageTk.PhotoImage(image=self.ImgPil)
        self.LblImage = Label(self.CointainerImgCuenta, image=self.Img, bg="white")
        self.LblImage.grid(row=1, column=1)
        self.ConteinerTxt = Frame(self.CointainerImgCuenta, bg="white")
        self.LblTipo = Label(self.ConteinerTxt, text=self.TipoCuenta, bg="white", font=self.FontBold,)
        self.LblCuenta = Label(self.ConteinerTxt, text=self.NumeroCuenta, bg="white", font=self.FontSaldoRegular, fg="#748699")
        self.LblTipo.pack()
        self.LblCuenta.pack(side=LEFT)
        self.ConteinerTxt.grid(row=1, column=2, padx=(10,0))
        self.CointainerImgCuenta.grid(row=1, column=1, padx=(0, 300))

        ##Dinero
        self.ConteinerDinero = Frame(self.ConteinerCuenta, bg="white")
        self.txtSaldo = StringVar()
        self.txtSaldo.set(str(self.Saldo))
        self.lblDinero = Label(self.ConteinerDinero, textvariable=self.txtSaldo, bg="white", font=self.FontBold)
        self.lblDinero.pack()
        self.lblTxt = Label(self.ConteinerDinero, text="Saldo Disponible", bg="white", font=self.FontDisponbleRegular)
        self.lblTxt.pack()
        self.ConteinerDinero.grid(row=1, column=2)
        self.ConteinerCuenta.pack(pady=(10,0))

    
    def Actualizar(self, saldo):
        self.txtSaldo.set(str(saldo))




