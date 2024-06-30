import tkinter as tk
from tkinter import ttk
import py_hot_reload

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo Treeview con Botón")
        self.geometry("600x400")

        # Crear Treeview
        self.tree = ttk.Treeview(self, columns=("col1", "col2", "col3"), show="headings")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Edad")
        self.tree.heading("col3", text="Acción")

        # Añadir datos de ejemplo
        self.tree.insert("", "end", values=("Alice", 30, "Ver Detalles"))
        self.tree.insert("", "end", values=("Bob", 25, "Ver Detalles"))

        # Configurar columna de acción para mostrar un botón (representado como texto)
        self.tree.column("col3", width=100, anchor=tk.CENTER)
        self.tree.bind("<Button-1>", self.on_tree_click)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def on_tree_click(self, event):
        item = self.tree.identify_row(event.y)
        print(item)
        if self.tree.identify_region(event.x, event.y) == "cell":
            column = self.tree.identify_column(event.x)
            if column == "#3":
                print(self.tree.item(item, 'values'))


def Main():
    app = App()
    app.mainloop()

py_hot_reload.run_with_reloader(Main)