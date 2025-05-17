#Atv1

import math

# Classe base
class Forma:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

# Classe derivada: Círculo
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

# Classe derivada: Retângulo
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

#Atv2

# Classe base
class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None

    def set_cor(self, cor):
        self.cor = cor
        return self  # permite encadeamento

    def set_modelo(self, modelo):
        self.modelo = modelo
        return self  # permite encadeamento

    def exibir_dados(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")

# Classe derivada: Carro
class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.portas = 4  # padrão

# Classe derivada: Bicicleta
class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = "urbana"  # padrão

#Atv3

class Calculadora:
    def somar(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError("A função somar aceita apenas dois inteiros ou duas strings.")


#Atv4
from abc import ABC, abstractmethod

# Interface Veiculo
class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

# Classe Carro que implementa Veiculo
class Carro(Veiculo):
    def acelerar(self):
        print("O carro está acelerando rapidamente.")

    def frear(self):
        print("O carro está freando com o pedal.")

# Classe Bicicleta que implementa Veiculo
class Bicicleta(Veiculo):
    def acelerar(self):
        print("A bicicleta está ganhando velocidade com o pedal.")

    def frear(self):
        print("A bicicleta está freando com o freio de mão.")

#Desafio

class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def resumo(self):
        print(f"Tipo de conta: Conta")
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0.0, taxa_manutencao=10.0, limite_cheque_especial=500.0):
        super().__init__(numero, titular, saldo)
        self.taxa_manutencao = taxa_manutencao
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if 0 < valor <= self.saldo + self.limite_cheque_especial:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso (incluindo cheque especial, se necessário).")
        else:
            print("Saque excede o limite disponível.")

    def resumo(self):
        print(f"Tipo de conta: Conta Corrente")
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Limite Cheque Especial: R${self.limite_cheque_especial:.2f}")
        print(f"Taxa de Manutenção: R${self.taxa_manutencao:.2f}")

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0.0, taxa_juros=0.03):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados com sucesso.")

    def resumo(self):
        print(f"Tipo de conta: Conta Poupança")
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Taxa de Juros: {self.taxa_juros * 100:.2f}%")

def main():
    print("=== Criando contas ===")
    conta1 = ContaCorrente("001", "João Silva", saldo=1000)
    conta2 = ContaPoupanca("002", "Maria Oliveira", saldo=2000)

    print("\n=== Operações com Conta Corrente ===")
    conta1.depositar(500)
    conta1.sacar(1800)
    conta1.exibir_saldo()
    conta1.resumo()

    print("\n=== Operações com Conta Poupança ===")
    conta2.depositar(1000)
    conta2.aplicar_juros()
    conta2.sacar(500)
    conta2.exibir_saldo()
    conta2.resumo()

if __name__ == "__main__":
    main()
