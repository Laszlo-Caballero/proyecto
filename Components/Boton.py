from tkinter import ttk, TOP
from PIL import Image, ImageTk

class Boton(ttk.Button):
    def __init__(self, parent, text, image_path= "", command=None):
        self.text = text
        self.image_path = image_path
        
        super().__init__(parent)

        style = ttk.Style()
        style.configure('Rounded.TButton', borderwidth=0, relief="flat", bordercolor="#000000")
        
        self.config(text=self.text, compound=TOP, style='Rounded.TButton', command= command)
        if(image_path != ""):
            image = Image.open(image_path)
            image = image.resize((32, 32))
            self.photo = ImageTk.PhotoImage(image)
            self.config(image=self.photo)
        
