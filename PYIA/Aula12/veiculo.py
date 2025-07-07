class Veiculo:
    def __init__(self):
        self.modelo = ""
        self.cor = ""
        self.ano = ""

    def set_modelo(self, modelo):
        self.modelo = modelo
        return self
    
    def set_cor(self, cor):
        self.cor = cor
        return self
    
    def set_ano(self, ano):
        self.ano = ano
        return self
    
    def __str__(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"
    
    
class Carro(Veiculo):
    def __init__(self):
        super().__init__()

    def exibir_carro(self):
        print(self.modelo, self.cor, self.ano)

class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()

carro = Carro().set_modelo("Jeep").set_cor("Azul").set_ano(2020)
carro.exibir_carro()