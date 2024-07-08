from tkinter import Toplevel, Label, ttk, Frame, Entry, Button
import tkinter as tk
import pickle
from Class.Usuario import Usuario
from .InterfazMovimientos import InterfazMovmientos

class InterfazAñadir(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Añadir Usuario")
        self.geometry("900x500")
        with open("Data/Usuario.pkl", 'rb') as file:
            self.datos_cargados: list[Usuario] = pickle.load(file)

        self.FramePrincipal = Frame(self)
        self.count = 0

        self.ContenedorForm = Frame(self.FramePrincipal)
        self.lbl = Label(self.ContenedorForm, text="Añadir Usuario")
        self.lbl.pack()
        self.lblNombre = Label(self.ContenedorForm, text="Nombre Completo")
        self.lblNombre.pack()
        self.txtNombre = Entry(self.ContenedorForm)
        self.txtNombre.pack(pady=10)
        self.lblNroCuenta = Label(self.ContenedorForm, text="Numero de cuenta")
        self.lblNroCuenta.pack()
        self.txtNroCuenta = Entry(self.ContenedorForm)
        self.txtNroCuenta.pack(pady=10)
        self.lblContraseña = Label(self.ContenedorForm, text="Contraseña")
        self.lblContraseña.pack()
        self.txtContraseña = Entry(self.ContenedorForm)
        self.txtContraseña.pack(pady=10)
        self.btnAñadir = Button(self.ContenedorForm, text="Añadir Usuario", command=self.AñadirUsuario)
        self.btnAñadir.pack()



        # Crear Tabla
        self.Tabla = ttk.Treeview(self.FramePrincipal, columns=("col1", "col2", "col3", "col4", "col5", "col6"), show='headings')
        headers = ["Nombre Cliente", "Numero de Cuenta", "Dni", "Contraseña", "Cantidad de dinero", "Moviminetos"]
        for i in range(len(headers)):
            self.Tabla.heading(f"col{i+1}", text=headers[i])
            self.Tabla.column(f"col{i+1}", anchor='center', width=150)
        self.CargarDatos()


        self.Tabla.bind("<Button-1>", self.VerMovimientos)
        self.Tabla.pack(expand=True, fill='both', side="right")

        self.ContenedorForm.pack(side='left', padx=(0,20))
        self.FramePrincipal.pack(expand=True)
    
    def VerMovimientos(self, event):
        item = self.Tabla.identify_row(event.y)
        column = self.Tabla.identify_column(event.x)
        if self.Tabla.identify_region(event.x, event.y) == "cell":
            if column == "#6":
                row_index =int(item[1:], 16) - self.count
                print(row_index)
                print(len(self.datos_cargados))
                print(self.datos_cargados[row_index -1].nombre)
                InterfazMovmientos(self.parent, self.datos_cargados[row_index -1].movimientos, self.datos_cargados[row_index -1].nombre)
    
    def Guardar(self):
        with open('Data/Usuario.pkl', 'wb') as file:
            pickle.dump(self.datos_cargados, file)
    
    def AñadirUsuario(self):
        Nombre = self.txtNombre.get()
        self.txtNombre.delete(0, tk.END)
        NumeroCuenta = self.txtNroCuenta.get()
        self.txtNroCuenta.delete(0, tk.END)
        contraseña = self.txtContraseña.get()
        self.txtContraseña.delete(0, tk.END)
        NuevoUsuario = Usuario(Nombre, NumeroCuenta, 0, [], contraseña)
        print(f"{Nombre=}, {NumeroCuenta=}, {contraseña=}")
        self.datos_cargados.append(NuevoUsuario)
        self.Guardar()
        self.CargarDatos()
        self.count += len(self.datos_cargados) -1
    
    def CargarDatos(self):
        for item in self.Tabla.get_children():
            self.Tabla.delete(item)
        for usuario in self.datos_cargados:
            self.Tabla.insert("", "end", values=(usuario.nombre, usuario.numeroCuenta, usuario.dni, usuario.contraseña, usuario.dinero, "Ver Movimientos"))
            
        
        
