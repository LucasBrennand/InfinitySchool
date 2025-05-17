#Atv1
import flet as ft

def main(page: ft.Page):
    page.title = "Personalização de Texto"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f5f5f5"

    # Texto 1 - Vermelho, negrito, grande
    texto1 = ft.Text(
        value="Texto Estilizado 1",
        color="red",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    # Texto 2 - Azul, tamanho médio, normal
    texto2 = ft.Text(
        value="Texto Estilizado 2",
        color="blue",
        size=24,
        weight=ft.FontWeight.NORMAL
    )

    # Texto 3 - Verde, pequeno, leve
    texto3 = ft.Text(
        value="Texto Estilizado 3",
        color="green",
        size=18,
        weight=ft.FontWeight.W_300  # Fonte mais leve
    )

    # Adicionando os textos à interface
    page.add(
        ft.Column(
            controls=[texto1, texto2, texto3],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# Executar o app
ft.app(target=main)

#Atv2
import flet as ft

def main(page: ft.Page):
    page.title = "Estilizando Botões"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f0f0f0"

    # Botão 1 - Vermelho com texto branco, grande
    botao1 = ft.ElevatedButton(
        text="Botão Vermelho",
        bgcolor="red",
        color="white",
        style=ft.ButtonStyle(
            padding=20,
            text_style=ft.TextStyle(size=20)
        )
    )

    # Botão 2 - Azul claro com texto escuro, médio
    botao2 = ft.FilledButton(
        text="Botão Azul Claro",
        bgcolor="#add8e6",
        color="#000080",
        style=ft.ButtonStyle(
            padding=15,
            text_style=ft.TextStyle(size=18)
        )
    )

    # Botão 3 - Verde com texto branco, pequeno
    botao3 = ft.OutlinedButton(
        text="Botão Verde",
        bgcolor="green",
        color="white",
        style=ft.ButtonStyle(
            padding=10,
            text_style=ft.TextStyle(size=16)
        )
    )

    # Adiciona os botões à tela
    page.add(
        ft.Column(
            controls=[botao1, botao2, botao3],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Executar o app
ft.app(target=main)


#Atv3
import flet as ft

def main(page: ft.Page):
    page.title = "Formulário Estilizado"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f9f9f9"

    # Campo de nome estilizado
    nome_input = ft.TextField(
        label="Nome",
        border_color="blue",
        focused_border_color="darkblue",
        cursor_color="blue",
        text_style=ft.TextStyle(size=16),
        width=300
    )

    # Campo de e-mail estilizado
    email_input = ft.TextField(
        label="Email",
        border_color="green",
        focused_border_color="darkgreen",
        cursor_color="green",
        text_style=ft.TextStyle(size=16),
        width=300
    )

    # Mensagem de resposta
    resposta = ft.Text(value="", color="black")

    # Função executada ao clicar no botão
    def enviar_dados(e):
        nome = nome_input.value
        email = email_input.value
        if nome and email:
            resposta.value = f"Obrigado, {nome}! Seu e-mail '{email}' foi recebido."
        else:
            resposta.value = "Por favor, preencha todos os campos."
        page.update()

    # Botão de envio estilizado
    botao_enviar = ft.ElevatedButton(
        text="Enviar",
        bgcolor="purple",
        color="white",
        style=ft.ButtonStyle(
            padding=15,
            text_style=ft.TextStyle(size=18),
            shape=ft.RoundedRectangleBorder(radius=8)
        ),
        on_click=enviar_dados
    )

    # Adiciona os elementos à tela
    page.add(
        ft.Column(
            controls=[
                nome_input,
                email_input,
                botao_enviar,
                resposta
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Executar o app
ft.app(target=main)

#Atv4
import flet as ft

def main(page: ft.Page):
    # Definição do tema personalizado
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE,
            secondary=ft.colors.AMBER,
            background=ft.colors.BLUE_GREY_50,
            on_background=ft.colors.BLACK,
            on_primary=ft.colors.WHITE,
            on_secondary=ft.colors.BLACK
        )
    )

    # Cor de fundo geral da página
    page.bgcolor = page.theme.color_scheme.background

    # Texto com cor personalizada
    texto = ft.Text(
        value="Bem-vindo à interface com tema personalizado!",
        size=20,
        color=page.theme.color_scheme.on_background
    )

    # Botão estilizado com cores do tema
    botao = ft.ElevatedButton(
        text="Clique aqui",
        bgcolor=page.theme.color_scheme.primary,
        color=page.theme.color_scheme.on_primary,
        style=ft.ButtonStyle(padding=15)
    )

    # Adicionando elementos à página
    page.add(
        ft.Column(
            controls=[texto, botao],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

# Executar o app
ft.app(target=main)

