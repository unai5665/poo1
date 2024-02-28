class alumno:
    def __init__(self, nombre, nota): 
        self.nota = nota
        self.nombre = nombre

    def imprimir(self):
        print(self.nombre,"obtiene:",self.nota)

    def promociona(self):
        if (self.nombre >= 5):
            print("promociona")
        else:
            print("va a ser que no") 