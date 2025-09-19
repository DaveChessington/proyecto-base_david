class Operaciones:
    def inputs(self,a,b):
        self.a=a
        self.b=b
        self.resultado=0

    def potencia(self):
        self.resultado=f"Potencia {self.a}**{self.b}={self.a**self.b}"

    def raiz(self):
        self.resultado=f"Raiz {self.a}sqrt{self.b}={self.a**(1/self.b)}"

    