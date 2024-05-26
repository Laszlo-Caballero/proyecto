from tkinter import *
from PIL import Image, ImageTk, ImageFont
from tkinter import ttk


class Boton:
    def __init__(self, contenedor) -> None:
        self.contenedor = contenedor
        self.contenedor.title("Button")
        self.contenedor.geometry("400x300")
        
        self.LoadCustomRegular = ImageFont.truetype("./font/Flexo-Regular-webfont.ttf", size=12)
        self.LoadCustomBold = ImageFont.truetype("./font/Flexo-Bold-webfont.ttf", size=12)
        self.LoadCustomDemi = ImageFont.truetype("./font/Flexo-Demi-webfont.ttf", size=12)
        
        self.contenedorBtn = Frame(self.contenedor)
        self.contenedorBtn.pack()
        self.paths = ["images/retiro.png", "images/depositar.png", "images/transferencia.png", "images/servicios.png"]
        self.btns = ["Retiro", "Depósitos", "Transferencia", "Servicios"]
        self.font=('Arial', 12)
        
        style = ttk.Style()
        style.configure('Rounded.TButton', borderwidth=0, relief="flat", bordercolor="#000000", font=self.font)
        
        for btn in range(len(self.btns)):
            img = Image.open(self.paths[btn])
            img = img.resize((30, 30))
            img = ImageTk.PhotoImage(img)
            boton = ttk.Button(self.contenedorBtn, text =self.btns[btn] , image = img, compound=TOP, style='Rounded.TButton')
            boton.image = img
            boton.grid(row=btn//2, column=btn%2, padx=5, pady=10, ipadx=20, ipady=20)
            
root = Tk()
Boton(root)
root.mainloop()

