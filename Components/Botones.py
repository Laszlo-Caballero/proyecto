from tkinter import *
from PIL import Image, ImageTk, ImageFont
from tkinter import ttk
from .Boton import Boton
from Class.Font import Font

class Botones(Frame):
    def __init__(self, root, Command) -> None:
        super().__init__(root)
        self.Command = Command
        self.LoadCustomRegular = ImageFont.truetype("./font/Flexo-Regular-webfont.ttf", size=12)
        self.LoadCustomBold = ImageFont.truetype("./font/Flexo-Bold-webfont.ttf", size=12)
        self.LoadCustomDemi = ImageFont.truetype("./font/Flexo-Demi-webfont.ttf", size=12)
        self.paths = ["images/retiro.png", "images/depositar.png", "images/transferencia.png", "images/servicios.png", "images/move.png"]
        self.btns = ["Retiro", "Depósitos", "Transferencia", "Servicios", "Ver Movimientos"]
        self.font=('Arial', 12)

        self.configure(background="white")
        style = ttk.Style()
        style.configure('Rounded.TButton', borderwidth=0, relief="flat", bordercolor="#000000", font=self.font)
        
        Label(self, text="Mis Servicios", background='white', font=Font(self, 10, Font="Bold").Font, foreground="#1f348d").grid(row=0, column=0, sticky='w', padx=(5,0), pady=(15,0))

        self.FrameBtn = Frame(self, bg='white')
        for btn in range(len(self.btns)):
            boton = Boton(self.FrameBtn, self.btns[btn], self.paths[btn], command=self.Command[btn])
            boton.grid(row=btn//2, column=btn%2, padx=5, pady=10, ipadx=20, ipady=20)
        
        self.FrameBtn.grid(row=1, column=0)


