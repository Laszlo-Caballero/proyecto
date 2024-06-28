from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import py_hot_reload

class MainPanel(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cajero")
        self.geometry("900x500")
        self.config(bg="white")
        
        self.ImgAñadirOpen = Image.open("images/agregar-usuario.png") 
        self.ImgAñadir = ImageTk.PhotoImage(self.ImgAñadirOpen)
        self.BtnAñadir = ttk.Button(self, text ="Añadir Cliente" , image = self.ImgAñadir, compound=TOP, style='Rounded.TButton')
        self.BtnAñadir.image = self.ImgAñadir
        self.BtnAñadir.pack()
        
        self.ImgCashOpen = Image.open("images/cash-report.png")
        self.ImgCash = ImageTk.PhotoImage(self.ImgCashOpen)
        self.BtnCash = ttk.Button(self, text ="Actualizar Dispensador" , image = self.ImgCash, compound=TOP, style='Rounded.TButton')
        self.BtnCash.image = self.ImgCash
        self.BtnCash.pack()


        self.BtnUsuario = [] 
        

def Main():
    app = MainPanel()
    app.mainloop()
py_hot_reload.run_with_reloader(Main)