class alumno:
    def imprimir(self):
        self.nombre ="" 
        self.nota = 0
        print(self.nombre,"obtiene:",self.nota)

    def promociona(self):
        self.nota = 0
        self.nombre = ""
        if (self.nombre >= 5):
            print("promociona")
        else:
            print("va a ser que no") 