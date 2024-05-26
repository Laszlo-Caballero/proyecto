import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class BCPApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BCP App")
        self.geometry("800x600")
        self.configure(background="#E5E5E5") 
       
        style = ttk.Style()
        style.configure("TFrame", background="#E5E5E5")
        style.configure("Header.TFrame", background="#003399")

        header_frame = ttk.Frame(self, style="Header.TFrame", height=100)
        header_frame.pack(fill="x")
       
        logo_image = Image.open("./images/bcp_logo.png")
        logo_image = logo_image.resize((50, 50))  
        self.logo_photo = ImageTk.PhotoImage(logo_image)
       
        logo_label = ttk.Label(header_frame, image=self.logo_photo, background="#003399")
        logo_label.pack(side="left", padx=10, pady=10)

        decorative_image = Image.open("./images/imagen__decorativa.png")
        decorative_image = decorative_image.resize((50, 50)) 
        self.decorative_photo = ImageTk.PhotoImage(decorative_image)

        decorative_label = ttk.Label(header_frame, image=self.decorative_photo, background="#003399")
        decorative_label.pack(side="right", padx=10, pady=10)

        main_frame = ttk.Frame(self, style="TFrame")
        main_frame.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = BCPApp()
    app.mainloop()