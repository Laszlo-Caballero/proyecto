from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk, ImageFont
#import py_hot_reload

class Header(Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.configure(background="#003399")
        self.pack(fill='x') 
       
        logo_image = Image.open("./images/bcp_logo.png")
        logo_image = logo_image.resize((100, 25))  
        self.logo_photo = ImageTk.PhotoImage(logo_image)
       
        logo_label = ttk.Label(self, image=self.logo_photo, background="#003399")
        logo_label.pack(side="left", padx=(20,0))
        self.LoadCustomDemi = ImageFont.truetype("./font/Flexo-Demi-webfont.ttf", size=12)
        self.FontDmi = font.Font(self, family=self.LoadCustomDemi.font, size=12, weight="bold")
        self.NombreTxt = Label(self, text="Hola, Laszlo", background="#003399", foreground="white", font=self.FontDmi)
        self.NombreTxt.pack(side="left", padx=(20,0))
        decorative_image = Image.open("./images/imagen__decorativa.png")
        decorative_image = decorative_image.resize((200, 100)) 
        self.decorative_photo = ImageTk.PhotoImage(decorative_image)

        decorative_label = ttk.Label(self, image=self.decorative_photo, background="#003399")
        decorative_label.pack(side="right")