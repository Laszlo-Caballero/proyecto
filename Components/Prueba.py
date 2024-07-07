import tkinter as ttk
from PIL import Image, ImageTk

class Prueba(ttk.Button):
    def __init__(self, parent, text, image_path, *args, **kwargs):
        self.font = ('Arial', 12)
        self.text = text
        self.image_path = image_path
        
        super().__init__(parent, *args, **kwargs)
        
        self.config(font=self.font, text=self.text, compound=ttk.LEFT, padx=10, pady=10)
        
        image = Image.open(image_path)
        image = image.resize((32, 32))
        self.photo = ImageTk.PhotoImage(image)
        self.config(image=self.photo)
        
