#Atv1
class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

# Exemplo de uso
meu_cachorro = Cachorro("Rex", "Labrador", 3)

print(f"Nome: {meu_cachorro.nome}")
print(f"Raça: {meu_cachorro.raca}")
print(f"Idade: {meu_cachorro.idade} anos")


#Atv2
class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

# Exemplo de uso
pessoa1 = Pessoa("Maria", 28, 62.5, "Feminino")

print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade} anos")
print(f"Peso: {pessoa1.peso} kg")
print(f"Gênero: {pessoa1.genero}")


#Atv3
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"Funcionário {funcionario.nome} adicionado com sucesso.")

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f"Funcionário {nome} removido com sucesso.")
                return
        print(f"Funcionário {nome} não encontrado.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            print(f"Lista de funcionários da empresa {self.nome}:")
            for funcionario in self.funcionarios:
                print(funcionario)

# Exemplo de uso
empresa = Empresa("Tech Solutions")

f1 = Funcionario("João", "Desenvolvedor", 4500)
f2 = Funcionario("Ana", "Designer", 3800)
f3 = Funcionario("Carlos", "Gerente", 6000)

empresa.adicionar_funcionario(f1)
empresa.adicionar_funcionario(f2)
empresa.adicionar_funcionario(f3)

empresa.listar_funcionarios()

empresa.remover_funcionario("Ana")

empresa.listar_funcionarios()


#Atv4
class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: divisão por zero."
        return a / b

# Exemplo de uso
calc = Calculadora()

print("Soma: ", calc.somar(10, 5))         # 15
print("Subtração: ", calc.subtrair(10, 5)) # 5
print("Multiplicação: ", calc.multiplicar(10, 5)) # 50
print("Divisão: ", calc.dividir(10, 5))    # 2.0
print("Divisão por zero: ", calc.dividir(10, 0))  # Erro


#Atv5
class Fatura:
    def __init__(self, nome_item, preco_unitario, quantidade):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0.0  # Inicializado como 0.0

    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade
        return self.valor_total

    def exibir_fatura(self):
        print(f"Item: {self.nome_item}")
        print(f"Preço unitário: R$ {self.preco_unitario:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Total da fatura: R$ {self.valor_total:.2f}")


#Desafio
class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario


class Quarto:
    def __init__(self, numero, preco_por_noite):
        self.numero = numero
        self.preco_por_noite = preco_por_noite
        self.reservado = False


class Reserva:
    def __init__(self, nome_cliente, noites, quarto: Quarto):
        self.nome_cliente = nome_cliente
        self.noites = noites
        self.quarto = quarto
        self.valor_total = self.calcular_valor()

    def calcular_valor(self):
        return self.noites * self.quarto.preco_por_noite


class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    # Funcionalidades dos funcionários
    def adicionar_funcionario(self, nome, funcao, salario):
        self.funcionarios.append(Funcionario(nome, funcao, salario))

    def listar_funcionarios(self):
        for f in self.funcionarios:
            print(f"{f.nome} - {f.funcao} - R$ {f.salario:.2f}")

    # Funcionalidades dos quartos
    def adicionar_quarto(self, numero, preco_por_noite):
        self.quartos.append(Quarto(numero, preco_por_noite))

    def listar_quartos_disponiveis(self):
        for q in self.quartos:
            if not q.reservado:
                print(f"Quarto {q.numero} - R$ {q.preco_por_noite:.2f} por noite")

    # Reservas
    def fazer_reserva(self, nome_cliente, numero_quarto, noites):
        for q in self.quartos:
            if q.numero == numero_quarto and not q.reservado:
                q.reservado = True
                reserva = Reserva(nome_cliente, noites, q)
                self.reservas.append(reserva)
                print(f"Reserva feita para {nome_cliente} no quarto {q.numero} por {noites} noites.")
                return
        print("Quarto não disponível ou inexistente.")

    def listar_reservas(self):
        for r in self.reservas:
            print(f"{r.nome_cliente} - Quarto {r.quarto.numero} - {r.noites} noites - Total: R$ {r.valor_total:.2f}")
