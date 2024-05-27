from tkinter import *
import py_hot_reload

class MainPanel(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cajero")
        self.geometry("700x500")
        self.config(bg="white")


def Main():
    app = MainPanel()
    app.mainloop()
py_hot_reload.run_with_reloader(Main)