from tkinter import *

class MainPanel:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cajero")
        self.ventana.geometry("500x500")
        self.ventana.config(bg="White")