from tkinter import *
from PIL import Image, ImageTk
import py_hot_reload

class Saldo:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.contenedor.title("Saldo")
        self.contenedor.geometry("500x200")
        self.TipoCuenta = "Ahorro"
        self.NumeroCuenta = "999123123"
        self.Saldo = "S/13"
        #Header
        self

        #Cuenta
        self.ConteinerCuenta = Frame(self.contenedor)
        self.imgPil = Image.open("./images/cosa.png").resize((50, 60))
        self.Img = ImageTk.PhotoImage(image=self.imgPil)
        self.ImgLabel = Label(self.ConteinerCuenta, image=self.Img)
        self.ImgLabel.grid(row=2, column=1)
        self.ConteinerTxt = Frame(self.contenedor)
        self.LblTipo = Label(self.ConteinerTxt, text=self.TipoCuenta)
        self.LblCuenta = Label(self.ConteinerTxt, text=self.NumeroCuenta)
        self.LblTipo.pack()
        self.LblCuenta.pack()
        self.ConteinerTxt.grid(row=2, column=2)
        self.ConteinerDinero = Frame(self.contenedor)
        self.lblDinero = Label(self.ConteinerDinero, text=self.Saldo)
        self.lblDinero.pack()
        self.lblTxt = Label(self.ConteinerDinero, text="Saldo Disponible")
        self.lblTxt.pack()
        self.ConteinerDinero.grid(row=2, column=3)


def Main():
    root = Tk()
    app = Saldo(root)
    root.mainloop()
py_hot_reload.run_with_reloader(Main)


