from tkinter import Toplevel, Label


class InterfazActualizar(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Actulizar Depostio")
        self.geometry("900x500")
        self.lbl = Label(self, text="Actualizar Deposito")
        self.lbl.pack()