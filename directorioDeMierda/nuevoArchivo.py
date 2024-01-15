class Perro:
    # constructor
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        print('pasando por getter')
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print('pasando por setter')
        if nombre.strip():
            self.__nombre = nombre


perro = Perro('Rodrigo')
# print(perro.get_nombre())
print(perro.nombre)
