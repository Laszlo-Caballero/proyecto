from Class.Movimiento import Movimiento
from Class.Usuario import Usuario
import pickle


Datos = [
     Usuario("Das", "999101", 12, [
         Movimiento("999101", "999102", 8, "Transferencia"),
         Movimiento("0", "99101", 20, "Deposito")
     ], "1234"),
     Usuario("Cas", "999102", 21, [
         Movimiento("0", "99102", 20, "Deposito"),
         Movimiento("999103", "999102", 1, "Transferencia")
     ], "1232"),
     Usuario("Mas", "999103", 10, [
         Movimiento("999103", "999102", 1, "Transferencia"),
         Movimiento("0", "99101", 20, "Deposito")
    ], "1234")
 ]
with open('Data/Usuario.pkl', 'wb') as file:
    pickle.dump(Datos, file)

