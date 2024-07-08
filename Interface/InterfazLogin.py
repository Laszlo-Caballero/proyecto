from tkinter import Toplevel, Label, Frame, Entry, Button
from PIL import Image, ImageTk, ImageFont
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from Class.Usuario import Usuario
from Class.Cajero import Cajero
import pickle
from Interface.InterfazUsuario import Cuenta

class Login(Toplevel):
    def __init__(self, parent, cajero):
        super().__init__(parent)
        self.title("Inicio de sesión")
        self.geometry("900x500")
        self.config(bg="white") 
        self.cajero = cajero
        
        with open(r"Data/Usuario.pkl", 'rb') as file:
            self.Usuarios: list[Usuario] = pickle.load(file)
        
        self.LoadCustomDemi = ImageFont.truetype("./font/Flexo-Demi-webfont.ttf", size=14)
        self.FontDmi = font.Font(self, family=self.LoadCustomDemi.font, size=14, weight="bold")

        image = Image.open("./images/login.png")
        image = image.resize((350, 500))  
        self.image_login = ImageTk.PhotoImage(image)
        
        self.image_label = Label(self, image = self.image_login)
        self.image_label.image = self.image_login
        self.image_label.pack( side ='left')
        
        self.frame_inicio = Frame(self, width = 470, height = 400, background='white')
        self.frame_inicio.pack(side="right", padx=40, pady=10)
        
        imageEntry = Image.open("./images/entry_img.png")
        imageEntry = imageEntry.resize((250, 50))
        self.image_entry = ImageTk.PhotoImage(imageEntry)
        
        self.inicio_label = Label(self.frame_inicio, text="Banca por Internet", foreground="#003399", background='white',font=self.FontDmi)
        self.inicio_label.place(x=145, y=25)
        
        self.dni_label = Label(self.frame_inicio, text="Documento de identidad", foreground="#003399",background='white', font=(self.FontDmi,12))
        self.dni_label .place(x=60, y=100)
        
        self.entryDni_label = Label(self.frame_inicio, image = self.image_entry, bd=0)
        self.entryDni_label.image = self.image_entry
        self.entryDni_label.place(x=110, y=135)
        
        self.txtDni =Entry(self.frame_inicio, width=35, bd=0)
        self.txtDni.place(x=120, y=150)
        
        self.pass_label = Label(self.frame_inicio, text="Contraseña", foreground="#003399",background='white', font=(self.FontDmi,12))
        self.pass_label.place(x=60, y=200)
        
        self.entryPass_label = Label(self.frame_inicio, image = self.image_entry, bd=0)
        self.entryPass_label.image = self.image_entry
        self.entryPass_label.place(x=110, y=230)
        
        self.txtContraseña = Entry(self.frame_inicio, width=35, bd = 0)
        self.txtContraseña.place(x=120, y=245)
        
        btnContinuar = Button(self.frame_inicio, text="Continuar", fg="white", bg="#F36F2C", borderwidth=0, relief="flat", width=30, font=(self.FontDmi,12), command= self.VerificarCuenta)
        btnContinuar.place(x=98, y=300)
        
    def VerificarCuenta(self):
        try:
            numero = int(self.txtDni.get())
            encontrado = False
            for usuario in self.Usuarios:
                if usuario.dni == self.txtDni.get():
                    encontrado = True
                    if usuario.contraseña == self.txtContraseña.get():
                        Cuenta(self, usuario, self.cajero)
                        break
                    else:
                        messagebox.showerror("Error", "Contraseña incorrecta")
                        break
            if not encontrado:
                messagebox.showerror("Error", "Cuenta no encontrada")
                
        except ValueError:
            messagebox.showerror("Error", "Debe insertar un número válido en el campo DNI")
