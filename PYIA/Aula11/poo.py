class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

class Empresa:
    def __init__(self):
        self.funcionarios = []
        pass

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def exibir_funcionario(self):
        for i in self.funcionarios:
              print(f"Funcionario: {i}")
      

    def remover_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)
        print(f"{funcionario.nome} removido com sucesso")
        
from funcionario import *
func1 = Funcionario("Lucas", "Dev", 800)
func2 = Funcionario("Mia", "Secretaria", 2000)
empresa = Empresa()
empresa.adicionar_funcionario(func1)
empresa.adicionar_funcionario(func2)
empresa.exibir_funcionario()
empresa.remover_funcionario(func1)
empresa.exibir_funcionario()
