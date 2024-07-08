from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

class ImageEntry(Frame):
    def __init__(self, parent, path, width = 28):
        super().__init__(parent)
        self.configure(background='white', bd=0, )
        image = Image.open(path)
        image = image.resize((200, 40))
        self.image_entry = ImageTk.PhotoImage(image)
        
        self.label = Label(self, image = self.image_entry, bd=0)
        self.label.image = self.image_entry
        self.label.pack(padx=2, pady=2)
        
        self.entry = Entry(self, width = width, bd = 0)
        self.entry.pack(padx=2, pady=2)
        self.entry.place(x=10, y = 12)

    def VerEntry(self):
        return self.entry.get()
    
    def ClearEntry(self):
        return self.entry.delete(0,tk.END)