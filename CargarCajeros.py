from Class.Cajero import Cajero
import pickle

Cajeros = [
    Cajero("Plaza Norte"),
    Cajero("Mall Plaza"),
    Cajero("Bcp"),
    Cajero("Tottus")
]

with open('Data/Cajero.pkl', 'wb') as file:
    pickle.dump(Cajeros, file)