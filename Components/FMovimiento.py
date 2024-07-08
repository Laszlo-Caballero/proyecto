from tkinter import Frame, Label
from Class.Movimiento import Movimiento
from Class.Font import Font

class FMovimiento(Frame):
    def __init__(self, root, movimiento : Movimiento):
        super().__init__(root)
        self.Tipo = movimiento.Tipo[0] ## Transfrencia T, R retiro
        self.Nombre = movimiento.Tipo 
        self.Fecha = movimiento.Fecha
        self.Monto = movimiento.Dinero
        self.config(bg='black')

        if (self.Tipo == "T" or self.Tipo == "R"):
            self.Monto = -self.Monto

        self.lbl1 = Label(self, text=self.Tipo, font=Font(self, 12, Font='Bold').Font)
        self.lbl1.grid(row=0, column=0, padx=(10,0))

        self.FrameTxt