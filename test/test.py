import tkinter as tk
from tkinter import Canvas

class CircularFrame(Canvas):
    def __init__(self, parent, diameter, **kwargs):
        Canvas.__init__(self, parent, width=diameter, height=diameter, **kwargs)
        self.diameter = diameter
        self.create_oval(0, 0, diameter, diameter, fill='blue', outline='blue')
        
    def place(self, **kwargs):
        Canvas.place(self, **kwargs)

class Example(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Circular Frame Example")
        self.geometry("400x400")
        self.config(bg="white")

root = tk.Tk()
example = Example(root)
circular_frame = CircularFrame(root, diameter=50)
circular_frame.place(relx=0.5, rely=0.5, anchor= tk.W)

        # Adding a label inside the circular frame
label = tk.Label(circular_frame, text="Hello", bg='blue', fg='white')
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.mainloop()
