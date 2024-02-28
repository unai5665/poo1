class alumno:
    def __init__(self): 
        self.nota = 0
        self.nombre = ""

    def imprimir(self):
        print(self.nombre,"obtiene:",self.nota)

    def promociona(self):
        if (self.nombre >= 5):
            print("promociona")
        else:
            print("va a ser que no") 