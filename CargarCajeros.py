from Class.Cajero import Cajero
import pickle

def Cargar():
    dato1 = Cajero("Plaza Norte")
    for billete in dato1.Billetes:
        billete.Cantidad = 23

    Cajeros = [
        dato1,
        Cajero("Mall Plaza"),
        Cajero("Bcp"),
        Cajero("Tottus")
    ]

    with open(r'Data/Cajero.pkl', 'wb') as file:
        pickle.dump(Cajeros, file)


