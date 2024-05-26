from tkinter import *

class Header:
    def __init__(self, contenedor = Tk()):
        self.contenedor = contenedor
        self.contenedor.title("Header")
        self.contenedor.geometry("500x20")


root = Tk()
Header(root)
root.mainloop()