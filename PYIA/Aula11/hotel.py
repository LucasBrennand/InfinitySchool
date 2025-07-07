class Hotel:
    def __init__(self):
        self.funcionarios = []
        self.quarto_reservado = None
        pass

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"{funcionario.nome} foi adicionado com sucesso")

    def remover_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)
        print(f"{funcionario.nome} removido com sucesso")

    def atualizar_salario(self, novo_salario, funcionario):
        funcionario.salario = novo_salario
        print(f"O novo salário de {funcionario.nome} é R${funcionario.salario}")

    def exibir_funcionarios(self):
        for i in self.funcionarios:
            print(f"Funcionario: {i}")

    def exibir_quartos(self, quarto):
        print(quarto)

    def reservar_quarto(self, quarto):
        if self.quarto_reservado != None:
            print(f"Já tem um quarto reservado")
        else:
            if (quarto.reservado == False):
                quarto.reservado = True
                self.quarto_reservado = quarto
                print(f"{quarto.numero} foi reservado")
            else:
                print(f"Esse quarto já está reservado")
            
            

class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}; Função: {self.funcao}; Salario: {self.salario}"
    
class Quarto:
    def __init__(self, numero, reservado):
        self.numero = numero
        self.reservado = reservado

    def __str__(self):
        return f"Número do quarto: {self.numero}; Reservado: {self.reservado}"

func1 = Funcionario("Lucas", "Faxineiro", 4000)
hotel = Hotel()
hotel.adicionar_funcionario(func1)
hotel.exibir_funcionarios()
hotel.atualizar_salario(5000, func1)
hotel.exibir_funcionarios()
quarto1 = Quarto(111, False)
quarto2 = Quarto(111, False)
print(quarto1)
hotel.reservar_quarto(quarto1)
print(quarto1)
hotel.reservar_quarto(quarto2)
print(quarto2)


