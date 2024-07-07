from tkinter import ttk, TOP
from PIL import Image, ImageTk

class Prueba(ttk.Button):
    def __init__(self, parent, text, image_path):
        self.text = text
        self.image_path = image_path
        
        super().__init__(parent)
        
        self.config(text=self.text, compound=TOP, style='Rounded.TButton')
        
        image = Image.open(image_path)
        image = image.resize((32, 32))
        self.photo = ImageTk.PhotoImage(image)
        self.config(image=self.photo)
        
