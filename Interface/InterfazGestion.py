from tkinter import Toplevel, Label, ttk, Frame, Entry, Button
import pickle
from Class.Usuario import Usuario
from Components.ImageEntry import ImageEntry
from Components.Mensaje import Mensaje
from .InterfazMovimientos import InterfazMovmientos
from .InterfazEditar import InterfazEditar
from tkinter import font
from PIL import Image, ImageTk, ImageFont


class InterfazGestion(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Añadir Usuario")
        self.geometry("1300x500")
        self.config(bg="white") 
        with open(r"Data/Usuario.pkl", 'rb') as file:
            self.datos_cargados: list[Usuario] = pickle.load(file)
            
        self.LoadCustomDemi = ImageFont.truetype("./font/Flexo-Demi-webfont.ttf", size=14)
        self.FontDmi = font.Font(self, family=self.LoadCustomDemi.font, size=14, weight="bold")
    
        self.frame_inicio = Frame(self, width = 1000, height = 200, background='white')
        self.frame_inicio.pack(side="top", padx=30, pady=10)
        self.count = 0
        
        imageEntry = Image.open("./images/entry_img.png")
        imageEntry = imageEntry.resize((250, 50))
        self.image_entry = ImageTk.PhotoImage(imageEntry) 
        
        self.lblAgregar = Label(self.frame_inicio, text="Agregar Usuario", foreground="#003399", background='white',font=self.FontDmi)
        self.lblAgregar.place(x=30, y=10)
        
        
        self.lblNombre = Label(self.frame_inicio, text="Agregar Nombre",foreground="#003399", font =(self.FontDmi,12), background='white')
        self.lblNombre.place(x=30, y = 60)
        
        self.txtNombre = ImageEntry(self.frame_inicio, "./images/entry_img.png" )
        self.txtNombre.place(x=25, y = 100)
        
        self.lblNroCuenta = Label(self.frame_inicio, text="Numero de Cuenta",foreground="#003399", font =(self.FontDmi,12), background='white' )
        self.lblNroCuenta.place(x= 290, y = 60)
        
        self.txtNroCuenta = ImageEntry(self.frame_inicio,"./images/entry_img.png" )
        self.txtNroCuenta.place(x=280 , y = 100)
        
        self.lblContraseña = Label(self.frame_inicio, text="Contraseña", foreground="#003399", font =(self.FontDmi,12), background='white')
        self.lblContraseña.place(x= 540, y = 60)
        
        self.txtContraseña = ImageEntry(self.frame_inicio,"./images/entry_img.png")
        self.txtContraseña.place(x= 530, y = 100)
        
        self.lblDni = Label(self.frame_inicio, text ="Documento de identidad",foreground="#003399", font =(self.FontDmi,12), background='white')
        self.lblDni.place(x=780, y = 60)
        
        self.txtDni = ImageEntry(self.frame_inicio,"./images/entry_img.png")
        self.txtDni.place(x=770, y = 100)
        
        self.lblBuscar = Label(self.frame_inicio, text ="Buscar", foreground="#003399", font =(self.FontDmi,12), background='white')
        self.lblBuscar.place(x = 550, y = 10)
        
        self.txtBuscar = ImageEntry(self,"./images/entry_img.png")
        self.txtBuscar.place(x=500, y = 420)
        
        self.combo = ttk.Combobox(self, values=["Nombre", "Dni", "Numero Cuenta"], width = 18, state="readonly", font =(self.FontDmi,10))
        self.combo.place(x = 730, y = 430)
        self.combo.current(0) 
        
        self.btnBuscar = Button(self, text="Buscar", fg="white", bg="#F36F2C", borderwidth=0, relief="flat", width=15, font=(self.FontDmi,11), command=self.Buscar)
        self.btnBuscar.place(x = 900, y = 430)
        
        self.frame_tabla = Frame(self, width = 1000, height = 300, background='red')
        self.frame_tabla.place(x= 55, y = 170)
        
        self.btnAgregar = Button(self, text = "Agregar Usuario", fg="white", bg="#F36F2C", borderwidth=0, relief="flat", width=25, font=(self.FontDmi,12),  command=self.AñadirUsuario)
        self.btnAgregar.place(x = 75, y = 430)
        


        
        self.Tabla = ttk.Treeview(self.frame_tabla, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"), show='headings')
        headers = ["Nombre Cliente", "Numero de Cuenta", "Dni", "Contraseña", "Cantidad de dinero", "Moviminetos", "Editar", "Eliminar"]
        for i in range(len(headers)):
            self.Tabla.heading(f"col{i+1}", text=headers[i])
            self.Tabla.column(f"col{i+1}", anchor='center', width=150)
        self.CargarDatos()
        
        self.Tabla.bind("<Button-1>", self.VerMovimientos)
        self.Tabla.pack(expand=True, fill='both', side="right")

        
    def VerMovimientos(self, event):
        item = self.Tabla.identify_row(event.y)
        column = self.Tabla.identify_column(event.x)
        if self.Tabla.identify_region(event.x, event.y) == "cell":
            if column == "#6" or column == "#7" or column == "#8":
                row_index =int(item[1:], 16) - self.count
                if column == "#6":
                    InterfazMovmientos(self.parent, self.datos_cargados[row_index -1].movimientos, self.datos_cargados[row_index -1].nombre)
                elif column == "#7":
                    top = InterfazEditar(self, self.datos_cargados[row_index -1])
                    top.protocol("WM_DELETE_WINDOW", lambda: self.on_toplevel_close(top))
                elif column == "#8":
                    self.Eliminar(row_index)
    
    def Guardar(self):
        with open(r'Data/Usuario.pkl', 'wb') as file:
            pickle.dump(self.datos_cargados, file)
            
    def on_toplevel_close(self, top: Toplevel):
        top.destroy()
        Usuario.Guardar(self.datos_cargados)
        self.count += len(self.datos_cargados)
        self.CargarDatos()

    def Buscar(self):
        criterio = self.combo.get()
        buscar = self.txtBuscar.VerEntry()
        
        if criterio == "Nombre":
            self.BuscarNombre(buscar)
        elif criterio == "Dni":
            self.BuscarDni(buscar)
        elif criterio == "Numero Cuenta":
            self.BuscarCuenta(buscar)
            
    def BuscarDni(self, dni):
        usuario_encontrado = None   
        
        for usuario in self.datos_cargados:
            if usuario.dni == dni:
                usuario_encontrado = usuario
                break
            
        if usuario_encontrado:
            self.Mostrar(usuario= usuario_encontrado)
        else:
            Mensaje(self, tipo='Error', mensaje= f"No se encontró ningún usuario con el dni {dni}.")

    def BuscarNombre(self, nombre):
        usuario_encontrado = None   
        
        for usuario in self.datos_cargados:
            if usuario.nombre == nombre:
                usuario_encontrado = usuario
                break
            
        if usuario_encontrado:
            self.Mostrar(usuario= usuario_encontrado)
        else:
            Mensaje(self, tipo='Error', mensaje= f"No se encontró ningún usuario con el nombre {nombre}.")
    
    def BuscarCuenta(self, cuenta):
        usuario_encontrado = None   
        
        for usuario in self.datos_cargados:
            if usuario.numeroCuenta == cuenta:
                usuario_encontrado = usuario
                break
            
        if usuario_encontrado:
            self.Mostrar(usuario= usuario_encontrado)
        else:
            Mensaje(self, tipo='Error', mensaje= f"No se encontró ningún usuario con la cuenta {cuenta}.")
    
    def Mostrar(self, usuario):
        datos_usuario = f"Nombre: {usuario.nombre} \n"
        datos_usuario += f"Numero de Cuenta: {usuario.numeroCuenta} \n"
        datos_usuario += f"Dni: {usuario.dni} \n"
        datos_usuario += f"Contraseña: {usuario.contraseña} \n"
        datos_usuario += f"Saldo: {usuario.dinero}"

        
        Mensaje(self, tipo = 'Check', mensaje=datos_usuario)
        
        
        
    def AñadirUsuario(self):
        Nombre = self.txtNombre.VerEntry()
        self.txtNombre.ClearEntry()
        NumeroCuenta = self.txtNroCuenta.VerEntry()
        self.txtNroCuenta.ClearEntry()
        contraseña = self.txtContraseña.VerEntry()
        self.txtContraseña.ClearEntry()
        dni =self.txtDni.VerEntry()
        self.txtDni.ClearEntry()
        NuevoUsuario = Usuario(Nombre, dni, NumeroCuenta, 0, [], contraseña)
        self.datos_cargados.append(NuevoUsuario)
        self.Guardar()
        self.CargarDatos()
        self.count += len(self.datos_cargados) -1
   
    def Eliminar(self, rowindex):
        self.count += len(self.datos_cargados)
        self.datos_cargados.pop(rowindex-1)
        Usuario.Guardar(self.datos_cargados)
        self.CargarDatos()
    
    def CargarDatos(self):
        for item in self.Tabla.get_children():
            self.Tabla.delete(item)
        for i in range(len(self.datos_cargados)):
            self.Tabla.insert("", i, values=(self.datos_cargados[i].nombre, self.datos_cargados[i].numeroCuenta, self.datos_cargados[i].dni, self.datos_cargados[i].contraseña, self.datos_cargados[i].dinero, "Ver Movimientos", "Editar", "Dar de baja"))







