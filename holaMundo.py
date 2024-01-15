class Perro:
    # constructor
    # def __init__(self, nombre):
    #     self.nombre = nombre
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f'{self.nombre} dice: Guau!!Guau!!')


# mi_perro = Perro('Chanchito')
# mi_perro2 = Perro('Rodrigo')
# print(mi_perro.nombre)
# print(mi_perro2.nombre)
mi_perro = Perro('Rodrigo', 2)
mi_perro.habla()

nombre = input("¿como se llama el payaso?: ")

print(f"el payaso se llama {nombre}")
