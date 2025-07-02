tarefas = []
def adicionar_tarefa():
    nome_tarefa = input("Digite uma nova tarefa: ")
    categoria_tarefa = input("Digite a categoria da tarefa: ")
    descricao_tarefa = input("Digite a descricao da tarefa: ")
    prioridade_tarefa = input("Digite a prioridade da tarefa (Baixo/ Alto): ")
    nova_tarefa = {
        "Nome": nome_tarefa,
        "Categoria": categoria_tarefa,
        "Descricao": descricao_tarefa,
        "Prioridade": prioridade_tarefa,
        "Concluida": False
    }
    tarefas.append(nova_tarefa)

def listar_tarefas():
    print(f"Todas as tarefas: {tarefas}")

def marcar_concluida(tarefa):
    nome_tarefa = input("Digite o nome tarefa para concluir: ")
    for i in tarefa:
        if (i["Nome"] == nome_tarefa):
            i["Concluida"] = True

def exibir_por_prioridade(tarefa):
    tarefas_filtradas = []
    prioridade_input = input("Qual priorade exibir? (Baixo/Alto):")
    for i in tarefa:
        if (i["Prioridade"].lower() == prioridade_input.lower()):
            tarefas_filtradas.append(i)
        print(tarefas_filtradas)

def exibir_por_categoria(tarefa):
    tarefas_filtradas = []
    categoria_input = input("Qual categoria exibir? :")
    for i in tarefa:
        if (i["Categoria"].lower() == categoria_input.lower()):
            tarefas_filtradas.append(i)
        print(tarefas_filtradas)

            
# adicionar_tarefa()
# exibir_por_prioridade(tarefas)
# exibir_por_categoria(tarefas)
# marcar_concluida(tarefas)
# listar_tarefas()

# MENU
op = 1
while(op != 0):
    op = int(input("""
               Digite uma opção: 
               1. Adicionar Tarefa
               2. Concluir Tarefa
               3. Exibir por Prioridade
               4. Exibir por Categoria
               5. Listar Tarefas
               0. Sair
               """))
    match op:
        case 1:
            adicionar_tarefa()
        case 2:
            marcar_concluida(tarefas)
        case 3: 
            exibir_por_prioridade(tarefas)
        case 4:
            exibir_por_categoria(tarefas)
        case 5:
            listar_tarefas()
        case 0:
            print("Saindo..")
        case _:
            print("Opção inválida")