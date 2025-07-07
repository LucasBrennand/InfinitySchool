# empresa.py
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome):
        for i in self.funcionarios:
            if i.nome.lower() == nome.lower():
                self.funcionarios.remove(i)
                print(f"Funcionário {nome} removido com sucesso!")
                return
        print(f"Funcionário {nome} não encontrado.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            for i in self.funcionarios:
                print(i)
