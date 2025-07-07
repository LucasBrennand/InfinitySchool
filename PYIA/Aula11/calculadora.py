class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        print(f"Soma: {self.numero1 + self.numero2}")
        return self.numero1 + self.numero2
    
    def subtracao(self):
        print(f"Subtração: {self.numero1 - self.numero2}")
        return self.numero1 - self.numero2
    
    def mult(self):
        print(f"Multiplicação: {self.numero1 * self.numero2}")
        return self.numero1 * self.numero2
    
    def div(self):
        print(f"Divisão: {self.numero1 / self.numero2}")
        return self.numero1 / self.numero2
    
calculadora = Calculadora(6, 3)
calculadora.soma()
calculadora.subtracao()
calculadora.mult()
calculadora.div()
    
