# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!\n")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
    else:
        for i, tarefa in enumerate(tarefas):
            concluida = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i+1}. Nome: {tarefa['nome']}\n   Descrição: {tarefa['descricao']}\n   Prioridade: {tarefa['prioridade']}\n   Categoria: {tarefa['categoria']}\n   Status: {concluida}\n")
        print()

# Função para marcar uma tarefa como concluída
def marcar_concluida(indice):
    try:
        tarefa = tarefas[indice]
        tarefa["concluida"] = True
        print(f"Tarefa '{tarefa['nome']}' marcada como concluída!\n")
    except IndexError:
        print("Índice inválido. Tarefa não encontrada.\n")

# Função para exibir tarefas por prioridade
def exibir_por_prioridade(prioridade):
    tarefas_filtradas = [t for t in tarefas if t['prioridade'] == prioridade]
    if tarefas_filtradas:
        for t in tarefas_filtradas:
            print(f"Nome: {t['nome']}\nDescrição: {t['descricao']}\nPrioridade: {t['prioridade']}\nCategoria: {t['categoria']}\n")
    else:
        print(f"Nenhuma tarefa com a prioridade '{prioridade}' encontrada.\n")

# Função para exibir tarefas por categoria
def exibir_por_categoria(categoria):
    tarefas_filtradas = [t for t in tarefas if t['categoria'] == categoria]
    if tarefas_filtradas:
        for t in tarefas_filtradas:
            print(f"Nome: {t['nome']}\nDescrição: {t['descricao']}\nPrioridade: {t['prioridade']}\nCategoria: {t['categoria']}\n")
    else:
        print(f"Nenhuma tarefa na categoria '{categoria}' encontrada.\n")

# Menu de comandos
def menu():
    while True:
        print("Menu de Comandos:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (Baixa, Média, Alta): ")
            categoria = input("Categoria (Ex: Trabalho, Casa, Estudo): ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        
        elif escolha == "2":
            listar_tarefas()
        
        elif escolha == "3":
            listar_tarefas()
            indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
            marcar_concluida(indice)
        
        elif escolha == "4":
            prioridade = input("Informe a prioridade (Baixa, Média, Alta): ")
            exibir_por_prioridade(prioridade)
        
        elif escolha == "5":
            categoria = input("Informe a categoria: ")
            exibir_por_categoria(categoria)
        
        elif escolha == "6":
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o menu
menu()
