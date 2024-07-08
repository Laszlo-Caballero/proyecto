from tkinter import Toplevel, Label, Frame, Entry, Button
from PIL import Image, ImageTk, ImageFont
from tkinter import font
from tkinter import ttk


class Login(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title="Inicio de sesión"
        self.geometry("900x500")
        self.config(bg="white") 
        
        self.LoadCustomDemi = ImageFont.truetype("./font/Flexo-Demi-webfont.ttf", size=14)
        self.FontDmi = font.Font(self, family=self.LoadCustomDemi.font, size=14, weight="bold")

        image = Image.open("./images/login.png")
        image = image.resize((350, 500))  
        self.image_login = ImageTk.PhotoImage(image)
        
        image_label = Label(self, image = self.image_login)
        image_label.image = self.image_login
        image_label.pack( side ='left')
        
        frame_inicio = Frame(self, width = 470, height = 400, background='white')
        frame_inicio.pack(side="right", padx=40, pady=10)
        
        imageEntry = Image.open("./images/entry_img.png")
        imageEntry = imageEntry.resize((250, 50))
        self.image_entry = ImageTk.PhotoImage(imageEntry)
        
        inicio_label = Label(frame_inicio, text="Banca por Internet", foreground="#003399", background='white',font=self.FontDmi)
        inicio_label.place(x=145, y=25)
        
        user_label = Label(frame_inicio, text="Numero de la Tarjeta", foreground="#003399",background='white', font=(self.FontDmi,12))
        user_label.place(x=60, y=100)
        
        entryUser_label = Label(frame_inicio, image = self.image_entry, bd=0)
        entryUser_label.image = self.image_entry
        entryUser_label.place(x=110, y=135)
        
        user_entry =Entry(frame_inicio, width=35, bd=0)
        user_entry.place(x=120, y=150)
        
        pass_label = Label(frame_inicio, text="Contraseña", foreground="#003399",background='white', font=(self.FontDmi,12))
        pass_label.place(x=60, y=200)
        
        entryPass_label = Label(frame_inicio, image = self.image_entry, bd=0)
        entryPass_label.image = self.image_entry
        entryPass_label.place(x=110, y=230)
        
        pass_entry = Entry(frame_inicio, width=35, bd = 0)
        pass_entry.place(x=120, y=245)
        
        btnContinuar = Button(frame_inicio, text="Continuar", fg="white", bg="#F36F2C", borderwidth=0, relief="flat", width=30, font=(self.FontDmi,12))
        btnContinuar.place(x=98, y=300)
        
            
        
        

        
        
        