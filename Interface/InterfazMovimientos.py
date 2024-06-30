from tkinter import Toplevel, ttk
from Class.Movimiento import Movimiento

class InterfazMovmientos(Toplevel):
    def __init__(self, parent, Movimientos : list[Movimiento], nombre):
        super().__init__(parent)
        self.movimientos = Movimientos
        self.title(f"Movimientos de {nombre}")
        self.geometry("900x500")
        self.config(bg="white")

        self.Tabla = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5"), show='headings')
        headers = ["Cuenta Origen", "Cuenta Destino", "Cantidad de Dinero", "Tipo de Movmiento", "Fecha"]
        for i in range(len(headers)):
            self.Tabla.heading(f"col{i+1}", text=headers[i])
            self.Tabla.column(f"col{i+1}", anchor='center', width=150)
        for usuario in self.movimientos:
            self.Tabla.insert("", "end", values=(usuario.CuentaOrigen, usuario.CuentaDestino, usuario.Dinero, usuario.Tipo, usuario.Fecha))            

        self.Tabla.pack(expand=True, fill='both')