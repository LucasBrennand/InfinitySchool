# #Atv1
# import flet as ft

# # Função que cria o formulário de cadastro
# def formulario_cadastro(page):

#     # Título do Formulário
#     page.add(ft.Text("Cadastro de Usuário", size=30, weight="bold", alignment="center"))

#     # Campos do Formulário
#     nome_input = ft.TextBox(label="Nome", autofocus=True)
#     sobrenome_input = ft.TextBox(label="Sobrenome")
#     email_input = ft.TextBox(label="E-mail")
#     telefone_input = ft.TextBox(label="Telefone")
#     endereco_input = ft.TextBox(label="Endereço")

#     # Função para processar o envio do formulário
#     def enviar_formulario(e):
#         nome = nome_input.value
#         sobrenome = sobrenome_input.value
#         email = email_input.value
#         telefone = telefone_input.value
#         endereco = endereco_input.value

#         # Exibe os dados do formulário após o envio
#         page.add(ft.Text(f"Cadastro realizado com sucesso!\n"
#                          f"Nome: {nome} {sobrenome}\n"
#                          f"E-mail: {email}\n"
#                          f"Telefone: {telefone}\n"
#                          f"Endereço: {endereco}", size=20))

#     # Botão de envio do formulário
#     enviar_button = ft.ElevatedButton("Enviar Cadastro", on_click=enviar_formulario)

#     # Organizando o layout com os widgets
#     form_layout = ft.Column(
#         controls=[nome_input, sobrenome_input, email_input, telefone_input, endereco_input, enviar_button],
#         spacing=15
#     )

#     # Adicionando o layout à página
#     page.add(form_layout)

# # Executando o Flet
# ft.app(target=formulario_cadastro)

# # #Atv2
# # import flet as ft

# # # Função para criar o aplicativo de lista de tarefas
# # def lista_de_tarefas(page):
# #     # Lista para armazenar as tarefas
# #     tarefas = []

# #     # Função para adicionar tarefa
# #     def adicionar_tarefa(e):
# #         tarefa = tarefa_input.value.strip()
# #         if tarefa != "":
# #             tarefas.append({"tarefa": tarefa, "concluida": False})
# #             tarefa_input.value = ""  # Limpa o campo de entrada
# #             atualizar_lista()  # Atualiza a lista de tarefas

# #     # Função para remover tarefa
# #     def remover_tarefa(tarefa_index):
# #         tarefas.pop(tarefa_index)
# #         atualizar_lista()

# #     # Função para marcar tarefa como concluída
# #     def marcar_concluida(tarefa_index):
# #         tarefas[tarefa_index]["concluida"] = not tarefas[tarefa_index]["concluida"]
# #         atualizar_lista()

# #     # Função para atualizar a lista de tarefas na tela
# #     def atualizar_lista():
# #         lista_tarefas.controls.clear()  # Limpa a lista atual
# #         for index, tarefa in enumerate(tarefas):
# #             texto_tarefa = f"{tarefa['tarefa']} - {'Concluída' if tarefa['concluida'] else 'Pendente'}"
            
# #             # Adiciona o texto da tarefa com opções para marcar como concluída e remover
# #             tarefa_item = ft.Row(
# #                 [
# #                     ft.Checkbox(value=tarefa["concluida"], on_change=lambda e, i=index: marcar_concluida(i)),
# #                     ft.Text(texto_tarefa),
# #                     ft.IconButton(ft.icons.DELETE, on_click=lambda e, i=index: remover_tarefa(i)),
# #                 ],
# #                 alignment="spaceBetween"
# #             )
# #             lista_tarefas.controls.append(tarefa_item)
# #         page.update()  # Atualiza a página com as mudanças na lista

# #     # Campo de entrada para nova tarefa
# #     tarefa_input = ft.TextBox(label="Nova Tarefa", autofocus=True)

# #     # Botão para adicionar tarefa
# #     adicionar_button = ft.ElevatedButton("Adicionar Tarefa", on_click=adicionar_tarefa)

# #     # Lista de tarefas
# #     lista_tarefas = ft.Column()

# #     # Layout do aplicativo
# #     page.add(
# #         ft.Column(
# #             controls=[
# #                 tarefa_input,
# #                 adicionar_button,
# #                 lista_tarefas,
# #             ],
# #             spacing=15
# #         )
# #     )

# # # Executando o Flet
# # ft.app(target=lista_de_tarefas)

# # #Atv3
# # import flet as ft

# # # Função que define o aplicativo da calculadora
# # def calculadora(page):
# #     # Variável para armazenar a expressão atual
# #     expressao = ft.Text(value="0")

# #     # Função para atualizar a expressão na tela
# #     def atualizar_expressao(valor):
# #         if expressao.value == "0":
# #             expressao.value = valor
# #         else:
# #             expressao.value += valor
# #         page.update()

# #     # Função para calcular e exibir o resultado
# #     def calcular(e):
# #         try:
# #             resultado = eval(expressao.value)
# #             expressao.value = str(resultado)
# #         except:
# #             expressao.value = "Erro"
# #         page.update()

# #     # Função para limpar a expressão
# #     def limpar(e):
# #         expressao.value = "0"
# #         page.update()

# #     # Layout da calculadora
# #     page.add(
# #         ft.Column(
# #             controls=[
# #                 # Display da calculadora
# #                 expressao,

# #                 # Linhas de botões para números e operações
# #                 ft.Row(
# #                     controls=[
# #                         ft.ElevatedButton("7", on_click=lambda e: atualizar_expressao("7")),
# #                         ft.ElevatedButton("8", on_click=lambda e: atualizar_expressao("8")),
# #                         ft.ElevatedButton("9", on_click=lambda e: atualizar_expressao("9")),
# #                         ft.ElevatedButton("/", on_click=lambda e: atualizar_expressao("/"))
# #                     ]
# #                 ),
# #                 ft.Row(
# #                     controls=[
# #                         ft.ElevatedButton("4", on_click=lambda e: atualizar_expressao("4")),
# #                         ft.ElevatedButton("5", on_click=lambda e: atualizar_expressao("5")),
# #                         ft.ElevatedButton("6", on_click=lambda e: atualizar_expressao("6")),
# #                         ft.ElevatedButton("*", on_click=lambda e: atualizar_expressao("*"))
# #                     ]
# #                 ),
# #                 ft.Row(
# #                     controls=[
# #                         ft.ElevatedButton("1", on_click=lambda e: atualizar_expressao("1")),
# #                         ft.ElevatedButton("2", on_click=lambda e: atualizar_expressao("2")),
# #                         ft.ElevatedButton("3", on_click=lambda e: atualizar_expressao("3")),
# #                         ft.ElevatedButton("-", on_click=lambda e: atualizar_expressao("-"))
# #                     ]
# #                 ),
# #                 ft.Row(
# #                     controls=[
# #                         ft.ElevatedButton("0", on_click=lambda e: atualizar_expressao("0")),
# #                         ft.ElevatedButton(".", on_click=lambda e: atualizar_expressao(".")),
# #                         ft.ElevatedButton("C", on_click=limpar),
# #                         ft.ElevatedButton("+", on_click=lambda e: atualizar_expressao("+"))
# #                     ]
# #                 ),
# #                 ft.Row(
# #                     controls=[
# #                         ft.ElevatedButton("=", on_click=calcular)
# #                     ]
# #                 ),
# #             ],
# #             alignment=ft.MainAxisAlignment.CENTER,
# #             spacing=10,
# #         )
# #     )

# # # Executa o Flet para iniciar o aplicativo
# # ft.app(target=calculadora)


# # #Atv4
import flet as ft

# Função para contar as palavras no texto
def contar_palavras(texto):
    return len(texto.split())

# Função principal do bloco de notas
def bloco_de_notas(page):
    # Definindo os controles principais: caixa de texto e botões
    texto = ft.TextBox(expand=True, multiline=True, autofocus=True, hint_text="Digite seu texto aqui...")
    palavras_label = ft.Text(value="Contagem de palavras: 0", size=14)
    
    # Função para salvar o conteúdo em um arquivo
    def salvar_texto(e):
        with open("nota.txt", "w") as file:
            file.write(texto.value)
        page.add(ft.SnackBar(ft.Text("Arquivo salvo com sucesso!")))
        page.update()

    # Função para abrir um arquivo e carregar o texto
    def abrir_texto(e):
        try:
            with open("nota.txt", "r") as file:
                texto.value = file.read()
            page.update()
        except FileNotFoundError:
            page.add(ft.SnackBar(ft.Text("Arquivo não encontrado!")))
            page.update()

    # Função para aplicar formatação de negrito
    def aplicar_negrito(e):
        texto.value = f"**{texto.value}**"
        page.update()

    # Função para aplicar formatação de itálico
    def aplicar_italico(e):
        texto.value = f"*{texto.value}*"
        page.update()

    # Atualizar a contagem de palavras sempre que o texto for alterado
    def atualizar_contagem(e):
        palavras_label.value = f"Contagem de palavras: {contar_palavras(texto.value)}"
        page.update()

    # Eventos para monitorar mudanças no texto
    texto.on_change = atualizar_contagem

    # Layout da interface do Bloco de Notas
    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Abrir", on_click=abrir_texto),
                        ft.ElevatedButton("Salvar", on_click=salvar_texto),
                        ft.ElevatedButton("Negrito", on_click=aplicar_negrito),
                        ft.ElevatedButton("Itálico", on_click=aplicar_italico),
                    ]
                ),
                texto,
                palavras_label
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )
    )

# Iniciar o aplicativo
ft.app(target=bloco_de_notas)

