from tkinter import Frame, Entry, StringVar, CENTER, DISABLED
from .Boton import Boton


class InputNumber(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.strCantidad = StringVar()
        self.strCantidad.set("0")

        self.txtMonto = Entry(self, textvariable=self.strCantidad)
        self.txtMonto.grid(row=0, column=0, ipady=10)

        self.FrameBtn = Frame(self)
        
        images = ["Images/up.png", "Images/down.png"]
        funciones = [self.Sumar, self.Restar]
        for i in range(len(images)):
            boton = Boton(self.FrameBtn, "", images[i],command=funciones[i], position=CENTER)
            boton.config(width=2)
            boton.grid_propagate(False)
            boton.grid(row=i, column=0)


        self.FrameBtn.grid(row=0, column=1)

    def Sumar(self):
        cant = int(self.strCantidad.get())
        cant += 1
        self.strCantidad.set(str(cant))

    def Restar(self):
        cant = int(self.strCantidad.get())
        if cant > 0:
            cant -= 1
            self.strCantidad.set(str(cant))
    

class CDinero(Frame):
    def __init__(self, parent, valor):
        super().__init__(parent)
        self.valor = valor

        self.boton = Boton(self, text=self.valor, position=CENTER)
        self.boton.config(state=DISABLED) 
        self.boton.grid(row=0, column=0, ipady=10)

        self.input = InputNumber(self)
        self.input.grid(row=0, column=1)

    
    def get_Cantidad(self):
        return self.input.strCantidad.get()
        




