
class Prueba:
    def __init__(self, nombre, dni) :
        self.nombre = nombre
        self.dni = dni
    
    def retornarnombre(self):
        return self.nombre, self.dni 


lista = [Prueba("wdasdasd", 1231231),Prueba("wdasdasd", 1231231),Prueba("wdasdasd", 1231231)]

dato = lista[0]

dato.nombre = "carlos"

nombre, dni = lista[0].retornarnombre()


dinero = 2580 // 200
cantidad = 2580 % 200


print(f"{x=} {y=}")