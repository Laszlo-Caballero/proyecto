from tkinter import *
from tkinter import font
from PIL import Image, ImageTk, ImageFont
import py_hot_reload

class Saldo:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.TipoCuenta = "Ahorro Soles"
        self.NumeroCuenta = "999123123"
        self.Saldo = "S/13.00"

        ##Font
        self.LoadCustomRegular = ImageFont.truetype("./font/Flexo-Regular-webfont.ttf", size=12)
        self.LoadCustomBold = ImageFont.truetype("./font/Flexo-Bold-webfont.ttf", size=12)
        self.LoadCustomDemi = ImageFont.truetype("./font/Flexo-Demi-webfont.ttf", size=12)
        self.FontRegular = font.Font(contenedor, family=self.LoadCustomRegular.font, size=12, weight="normal")
        self.FontDisponbleRegular = font.Font(contenedor, family=self.LoadCustomRegular.font, size=8, weight="normal")
        self.FontSaldoRegular = font.Font(contenedor, family=self.LoadCustomRegular.font, size=9, weight="normal")  
        self.FontBold = font.Font(contenedor, family=self.LoadCustomBold.font, size=10, weight="bold")
        self.FontDmi = font.Font(contenedor, family=self.LoadCustomDemi.font, size=12, weight="bold")
        #Header
        self.CointainerHeader = Frame(self.contenedor)
        self.CointainerHeader.config(bg="white")
        self.LblProductos = Label(self.CointainerHeader, text="Mis Productos", bg="white", font=self.FontRegular, fg="#1f348d")
        self.LblProductos.grid(row=1, column=1, padx=(0, 230))
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
        self.ConteinerCuenta = Frame(self.contenedor, bg="white")
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
        self.CointainerImgCuenta.grid(row=1, column=1, padx=(0, 150))

        ##Dinero
        self.ConteinerDinero = Frame(self.ConteinerCuenta, bg="white")
        self.lblDinero = Label(self.ConteinerDinero, text=self.Saldo, bg="white", font=self.FontBold)
        self.lblDinero.pack()
        self.lblTxt = Label(self.ConteinerDinero, text="Saldo Disponible", bg="white", font=self.FontDisponbleRegular)
        self.lblTxt.pack()
        self.ConteinerDinero.grid(row=1, column=2)
        self.ConteinerCuenta.pack(pady=(10,0))

def Main():
    root = Tk()
    root.geometry("500x200")
    root.title("Saldo")
    contenedor = Frame(root)
    contenedor.config(bg="white")
    app = Saldo(contenedor)
    contenedor.pack()
    root.mainloop()
py_hot_reload.run_with_reloader(Main)


