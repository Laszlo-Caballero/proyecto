from Class.Movimiento import Movimiento
from Class.Usuario import Usuario
import pickle


Datos = [
     Usuario("Das", "082012025", "999101", 12, [
         Movimiento("999101", "999102", 8, "Transferencia"),
         Movimiento("0", "99101", 4, "Deposito")
     ], "1234"),
     Usuario("Cas", "082012225", "999102", 300000, [
         Movimiento("0", "99102", 20, "Deposito"),
         Movimiento("999103", "999102", 1, "Transferencia")
     ], "1232"),
     Usuario("Mas", "082013025", "999103", 10, [
         Movimiento("999103", "999102", 1, "Transferencia"),
         Movimiento("0", "99101", 20, "Deposito")
    ], "1234")
 ]


with open(r'Data/Usuario.pkl', 'wb') as file:
    pickle.dump(Datos, file)




