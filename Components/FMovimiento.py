from tkinter import Frame, Label, Entry
from Class.Movimiento import Movimiento
from Class.Font import Font
import locale
from datetime import datetime

class FMovimiento(Frame):
    def __init__(self, root, movimiento : Movimiento, numeroOriginal):

        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        super().__init__(root)
        self.Tipo = movimiento.Tipo[0] ## Transfrencia T, R retiro
        self.Nombre = movimiento.Tipo
        print(self.Nombre)
        self.Fecha = movimiento.Fecha
        self.Monto = movimiento.Dinero
        self.movimiento = movimiento
        self.FontColor = "black"
        self.config(bg='white')
        meses_espanol = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


        if (self.Tipo == "R" or self.Tipo == "P"):
            self.Monto = -self.Monto
            self.FontColor = "red"
        elif(self.Tipo =="T"):
            if self.movimiento.CuentaOrigen == numeroOriginal:
                self.FontColor = "red"

        self.lbl1 = Label(self, text=self.Tipo, font=Font(self, 15, Font='Bold').Font, bg='blue', foreground='white')
        self.lbl1.grid(row=0, column=0, padx=(10,10), ipadx=10, ipady=8)

        self.FrameTxt = Frame(self, background='white')
        
        self.lbl2 = Label(self.FrameTxt, text=self.Nombre, font=Font(self, 15, Font='Bold').Font, background='white')
        self.lbl2.grid(row=0, column=0)

        self.lbl3 = Label(self.FrameTxt, text=f"{self.Fecha.day} {meses_espanol[self.Fecha.month - 1]}", background='white')
        self.lbl3.grid(row=1, column=0, sticky='w')

        self.FrameTxt.grid(row=0, column=1)
        
        self.lbl4 = Label(self, text=f"S/ {self.Monto}", foreground=self.FontColor, font=Font(self, 15, Font='Bold').Font, background='white')

        self.lbl4.grid(row=0, column=2, padx=(50,0))