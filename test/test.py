import tkinter as tk
from tkinter import ttk

def validate_numeric_input(action, index, value_if_allowed,
                           prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789.-+':  # Permite dígitos, punto decimal, signo negativo y positivo
        try:
            float(value_if_allowed)  # Intenta convertir el valor a float
            return True
        except ValueError:
            return False
    else:
        return False

root = tk.Tk()
root.geometry("300x200")

# Crear una validación en el widget Entry
vcmd = (root.register(validate_numeric_input), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

# Crear un ttk.Entry con la validación
entry = ttk.Entry(root, validate='key', validatecommand=vcmd)
entry.pack(pady=20)

root.mainloop()
