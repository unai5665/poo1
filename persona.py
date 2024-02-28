class Persona:
    def __init__(self, nombre, anios):
        self.nombre = ""
        self.anios = 0

    def imprimir(self):
        print(self.nombre,"tiene:",self.anios,"años")


    def cumpleanios(self):
        self.edad += 1
        self.imprimir()

if __name__ == "__main__":
    obama = Persona("Obama", 62)
    obama.imprimir()
    obama.cumpleanios()
        