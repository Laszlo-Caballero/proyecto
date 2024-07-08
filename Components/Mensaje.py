from tkinter import Toplevel, Label
from PIL import Image, ImageTk

class Mensaje(Toplevel):
    def __init__(self, parent, tipo=('Check', 'Advertencia', 'Error'), mensaje = ""):
        super().__init__(parent)
        
        self.geometry("700x200")
        self.tipo = tipo
        self.title(tipo)
        
        if tipo == 'Check':
            image = Image.open("./images/comprobado.png")
            self.imagenFr = ImageTk.PhotoImage(image)
        elif tipo == 'Advertencia':
            image = Image.open("./images/advertencia.png")
            self.imagenFr = ImageTk.PhotoImage(image) 
        elif tipo == 'Error':
            image = Image.open("./images/cerrar.png")
            self.imagenFr = ImageTk.PhotoImage(image) 
        
        self.label = Label(self, image = self.imagenFr, bd=0)  
        self.label.image = self.imagenFr
        self.label.place(x=10, y = 12)
        
        self.Mensaje = Label(self, text = mensaje, font =('Arial', 11),foreground="#003399")
        self.Mensaje.place(x=100, y = 30)
    