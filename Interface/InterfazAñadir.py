from tkinter import Toplevel, Label


class InterfaUsuario(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Añadir Usuario")
        self.geometry("400x300")
        self.lbl = Label(self, text="Añadir Usuario")
        self.lbl.pack()