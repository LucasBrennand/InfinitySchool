class Veiculo:
    def __init__(self):
        pass

    def acelerar(self):
        return ""
    
    def frear(self):
        return ""
    
class Carro(Veiculo):
    def __init__(self, veiculo):
        self.veiculo = veiculo

    def acelerar(self):
        return f"{self.veiculo} está acelerando"
    
    def frear(self):
        return f"{self.veiculo} está freando"

class Bicicleta(Veiculo):
    def __init__(self, veiculo):
        self.veiculo = veiculo

    def acelerar(self):
        return f"A {self.veiculo} está acelerando"
    
    def frear(self):
        return f"A {self.veiculo} está freando"
    
carro = Carro("Renegade")
bicicleta = Bicicleta("Brmax")





print(carro.acelerar())
print(carro.frear())
print(bicicleta.acelerar())
print(bicicleta.frear())