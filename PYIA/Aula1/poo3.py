#Atv1

class Tarefa:
    def __init__(self, titulo, descricao, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def marcar_como_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"Tarefa: {self.titulo} | Status: {status}\nDescrição: {self.descricao}"

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        if isinstance(tarefa, Tarefa):
            self.tarefas.append(tarefa)
        else:
            print("Erro: somente objetos da classe Tarefa podem ser adicionados.")

    def listar_tarefas(self):
        print(f"\nProjeto: {self.nome}")
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(self.tarefas, start=1):
                print(f"{i}. {tarefa}")

def main():
    # Criando projeto
    projeto1 = Projeto("Projeto Python")

    # Criando tarefas
    tarefa1 = Tarefa("Criar classe Tarefa", "Definir título, descrição e status.")
    tarefa2 = Tarefa("Criar classe Projeto", "Permitir associar tarefas ao projeto.")
    tarefa3 = Tarefa("Testar funcionalidades", "Executar o código e verificar tudo.")

    # Associando tarefas ao projeto
    projeto1.adicionar_tarefa(tarefa1)
    projeto1.adicionar_tarefa(tarefa2)
    projeto1.adicionar_tarefa(tarefa3)

    # Marcando uma tarefa como concluída
    tarefa2.marcar_como_concluida()

    # Listando tarefas do projeto
    projeto1.listar_tarefas()

if __name__ == "__main__":
    main()


#Atv2

class Pedido:
    def __init__(self, id_pedido, itens, valor_total, cliente=None):
        self.id_pedido = id_pedido
        self.itens = itens  # Lista de strings (nomes dos itens)
        self.valor_total = valor_total
        self.cliente = cliente  # Associação ao objeto Cliente

    def __str__(self):
        return f"Pedido #{self.id_pedido} | Itens: {', '.join(self.itens)} | Valor: R${self.valor_total:.2f}"

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.pedidos = []  # Lista de objetos Pedido

    def fazer_pedido(self, pedido):
        pedido.cliente = self  # Define a associação reversa
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        print(f"\nPedidos de {self.nome}:")
        if not self.pedidos:
            print("Nenhum pedido encontrado.")
        else:
            for pedido in self.pedidos:
                print(pedido)

def main():
    # Criando clientes
    cliente1 = Cliente("Alice", "alice@email.com")
    cliente2 = Cliente("Bob", "bob@email.com")

    # Criando pedidos
    pedido1 = Pedido(101, ["Camisa", "Calça"], 120.50)
    pedido2 = Pedido(102, ["Tênis"], 200.00)
    pedido3 = Pedido(103, ["Boné", "Cinto"], 75.30)

    # Associando pedidos aos clientes
    cliente1.fazer_pedido(pedido1)
    cliente1.fazer_pedido(pedido3)
    cliente2.fazer_pedido(pedido2)

    # Listando os pedidos de cada cliente
    cliente1.listar_pedidos()
    cliente2.listar_pedidos()

if __name__ == "__main__":
    main()


#Atv3

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome         # Atributo privado
        self.__idade = idade       # Atributo privado
        self.__matricula = matricula  # Atributo privado

    # Getters
    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_matricula(self):
        return self.__matricula

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_matricula(self, matricula):
        self.__matricula = matricula

    # Método para exibir os dados do aluno
    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")
        print(f"Matrícula: {self.__matricula}")


def main():
    # Criando um aluno
    aluno1 = Aluno("João", 20, "A1234")

    # Exibindo os dados iniciais
    print("Dados do aluno:")
    aluno1.exibir_dados()

    # Modificando os dados
    aluno1.set_nome("João Silva")
    aluno1.set_idade(21)
    aluno1.set_matricula("B5678")

    # Exibindo os dados atualizados
    print("\nDados atualizados:")
    aluno1.exibir_dados()

if __name__ == "__main__":
    main()

#Atv4

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.set_preco(preco)
        self.set_quantidade(quantidade)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: O preço não pode ser negativo.")

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            print("Erro: A quantidade não pode ser negativa.")

    # Método para exibir as informações do produto
    def exibir_produto(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Quantidade em estoque: {self.__quantidade}")

def main():
    # Criando o produto
    produto1 = Produto("Notebook", 3500.00, 10)
    produto1.exibir_produto()

    # Tentando definir valores inválidos
    produto1.set_preco(-100)
    produto1.set_quantidade(-5)

    # Atualizando com valores válidos
    produto1.set_preco(3300.00)
    produto1.set_quantidade(15)

    print("\nProduto atualizado:")
    produto1.exibir_produto()

if __name__ == "__main__":
    main()

#Atv5

class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0):
        self.__numero_conta = numero_conta
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0
        self.__transacoes = []
        if saldo_inicial > 0:
            self.__transacoes.append(f"Depósito inicial: R$ {saldo_inicial:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__transacoes.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Erro: Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                self.__transacoes.append(f"Saque: R$ {valor:.2f}")
            else:
                print("Erro: Saldo insuficiente para saque.")
        else:
            print("Erro: Valor de saque deve ser positivo.")

    def verificar_saldo(self):
        return self.__saldo

    def extrato(self):
        print(f"\nExtrato da Conta {self.__numero_conta}:")
        for t in self.__transacoes:
            print(t)
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

def main():
    conta = ContaBancaria("12345", 1000)

    conta.depositar(500)
    conta.sacar(200)
    conta.sacar(2000)  # tentativa inválida
    conta.depositar(-50)  # tentativa inválida

    print(f"\nSaldo atual: R$ {conta.verificar_saldo():.2f}")
    conta.extrato()

if __name__ == "__main__":
    main()

#Desafio

class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor


class Usuario:
    def __init__(self, nome, id_usuario):
        self.__nome = nome
        self.__id_usuario = id_usuario

    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id_usuario

    def set_nome(self, novo_nome):
        self.__nome = novo_nome


class Biblioteca:
    def __init__(self):
        self.__livros_disponiveis = []

    def adicionar_livro(self, livro):
        self.__livros_disponiveis.append(livro)
        print(f'Livro "{livro.get_titulo()}" adicionado à biblioteca.')

    def remover_livro(self, livro):
        if livro in self.__livros_disponiveis:
            self.__livros_disponiveis.remove(livro)
            print(f'Livro "{livro.get_titulo()}" removido da biblioteca.')
        else:
            print(f'Livro "{livro.get_titulo()}" não está disponível na biblioteca.')

    def listar_livros(self):
        if not self.__livros_disponiveis:
            print("Nenhum livro disponível na biblioteca.")
        else:
            print("Livros disponíveis na biblioteca:")
            for livro in self.__livros_disponiveis:
                print(f' - {livro.get_titulo()} de {livro.get_autor()}')

    def livro_disponivel(self, livro):
        return livro in self.__livros_disponiveis


class Emprestimo:
    def __init__(self, usuario, livro, biblioteca):
        self.__usuario = usuario
        self.__livro = livro
        self.__biblioteca = biblioteca
        self.__ativo = False

    def registrar(self):
        if self.__biblioteca.livro_disponivel(self.__livro):
            self.__biblioteca.remover_livro(self.__livro)
            self.__ativo = True
            print(f'Empréstimo registrado: "{self.__livro.get_titulo()}" para {self.__usuario.get_nome()}.')
        else:
            print(f'Livro "{self.__livro.get_titulo()}" não está disponível para empréstimo.')

    def exibir_info(self):
        status = "ativo" if self.__ativo else "inativo"
        print(f'Empréstimo {status}: Livro "{self.__livro.get_titulo()}" emprestado para {self.__usuario.get_nome()} (ID: {self.__usuario.get_id()}).')

def main():
    # Criar livros
    livro1 = Livro("1984", "George Orwell")
    livro2 = Livro("Dom Casmurro", "Machado de Assis")
    livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

    # Criar usuários
    usuario1 = Usuario("Alice", 101)
    usuario2 = Usuario("Bruno", 102)

    # Criar biblioteca e adicionar livros
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    biblioteca.listar_livros()

    # Registrar empréstimo
    emprestimo1 = Emprestimo(usuario1, livro1, biblioteca)
    emprestimo1.registrar()
    emprestimo1.exibir_info()

    biblioteca.listar_livros()

    # Tentar emprestar livro já emprestado
    emprestimo2 = Emprestimo(usuario2, livro1, biblioteca)
    emprestimo2.registrar()

    # Emprestar outro livro
    emprestimo3 = Emprestimo(usuario2, livro2, biblioteca)
    emprestimo3.registrar()
    emprestimo3.exibir_info()

    biblioteca.listar_livros()


if __name__ == "__main__":
    main()
