import tkinter as tk
from tkinter import ttk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo de cambiar la fuente de un ttk.Button")

        # Crear un botón
        self.boton = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.boton.pack(pady=20, padx=50)

        # Cambiar la fuente del botón después de crearlo
        self.boton.configure(style='my.TButton')

        # Crear un estilo personalizado para el botón
        self.style = ttk.Style()
        self.style.configure('my.TButton', font=('Arial', 12))

    def on_button_click(self):
        print("Botón clickeado")

# Crear la ventana principal y ejecutar la aplicación
app = Aplicacion()
app.mainloop()
