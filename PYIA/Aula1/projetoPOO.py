class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    # Getters e setters com validação simples
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome:
            self.__nome = nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Método polimórfico
    def exibir_informacoes(self):
        return f"Nome: {self.__nome}\nTelefone: {self.__telefone}\nEmail: {self.__email}"


class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, id_cliente):
        super().__init__(nome, telefone, email)
        self.__id_cliente = id_cliente

    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def exibir_informacoes(self):
        info = super().exibir_informacoes()
        return f"{info}\nID Cliente: {self.__id_cliente}"

class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco_diaria = preco_diaria
        self.__disponivel = True

    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def get_preco_diaria(self):
        return self.__preco_diaria

    def is_disponivel(self):
        return self.__disponivel

    def set_disponivel(self, status):
        self.__disponivel = status

    def exibir_informacoes(self):
        status = "Disponível" if self.__disponivel else "Ocupado"
        return f"Quarto {self.__numero} - {self.__tipo} - R$ {self.__preco_diaria:.2f} - {status}"

from datetime import datetime

class Reserva:
    def __init__(self, cliente, quarto, checkin, checkout):
        self.__cliente = cliente
        self.__quarto = quarto
        self.__checkin = checkin
        self.__checkout = checkout
        self.__status = "Ativa"

    def get_cliente(self):
        return self.__cliente

    def get_quarto(self):
        return self.__quarto

    def get_checkin(self):
        return self.__checkin

    def get_checkout(self):
        return self.__checkout

    def get_status(self):
        return self.__status

    def cancelar(self):
        self.__status = "Cancelada"
        self.__quarto.set_disponivel(True)

    def exibir_informacoes(self):
        return (f"Reserva: {self.__cliente.get_nome()} - Quarto {self.__quarto.get_numero()} ({self.__quarto.get_tipo()})\n"
                f"Check-in: {self.__checkin.strftime('%d/%m/%Y')} | Check-out: {self.__checkout.strftime('%d/%m/%Y')}\n"
                f"Status: {self.__status}")
    
class GerenciadorDeReservas:
    def __init__(self):
        self.__clientes = []
        self.__quartos = []
        self.__reservas = []

    # Métodos para gerenciar clientes
    def adicionar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def listar_clientes(self):
        return self.__clientes

    def buscar_cliente_por_id(self, id_cliente):
        for cliente in self.__clientes:
            if cliente.get_id_cliente() == id_cliente:
                return cliente
        return None

    # Métodos para gerenciar quartos
    def adicionar_quarto(self, quarto):
        self.__quartos.append(quarto)

    def listar_quartos(self):
        return self.__quartos

    def quartos_disponiveis(self):
        return [q for q in self.__quartos if q.is_disponivel()]

    # Métodos para gerenciar reservas
    def criar_reserva(self, cliente, quarto, checkin, checkout):
        if quarto.is_disponivel():
            reserva = Reserva(cliente, quarto, checkin, checkout)
            quarto.set_disponivel(False)
            self.__reservas.append(reserva)
            return reserva
        else:
            return None

    def cancelar_reserva(self, reserva):
        reserva.cancelar()

    def listar_reservas(self):
        return self.__reservas


import flet
from flet import Page, Text, ElevatedButton, ListView, TextField, Dropdown, DropdownMenuItem, DatePicker, AlertDialog, Column, Row

def main(page: Page):
    page.title = "Refúgio dos Sonhos - Gerenciador de Reservas"
    page.vertical_alignment = "start"
    page.padding = 20

    gerenciador = GerenciadorDeReservas()

    # Adicionando quartos exemplo
    gerenciador.adicionar_quarto(Quarto(101, "Single", 200))
    gerenciador.adicionar_quarto(Quarto(102, "Double", 350))
    gerenciador.adicionar_quarto(Quarto(201, "Suite", 600))

    # Adicionando clientes exemplo
    gerenciador.adicionar_cliente(Cliente("Alice", "99999-0000", "alice@mail.com", 1))
    gerenciador.adicionar_cliente(Cliente("Bruno", "98888-1111", "bruno@mail.com", 2))

    # --- Definir telas ---
    # Tela inicial: lista quartos, botões
    def tela_inicial():
        page.clean()

        titulo = Text("Quartos do Refúgio dos Sonhos", size=24, weight="bold")
        lista_quartos = ListView(
            expand=True,
            spacing=5,
            auto_scroll=False,
            controls=[
                Text(q.exibir_informacoes()) for q in gerenciador.listar_quartos()
            ]
        )

        btn_reservar = ElevatedButton("Fazer Reserva", on_click=lambda e: tela_reserva())
        btn_clientes = ElevatedButton("Gerenciar Clientes", on_click=lambda e: tela_clientes())
        btn_reservas = ElevatedButton("Ver Reservas", on_click=lambda e: tela_reservas())

        page.add(
            titulo,
            lista_quartos,
            Row([btn_reservar, btn_clientes, btn_reservas], alignment="spaceAround"),
        )

    # Tela de reservas
    def tela_reservas():
        page.clean()

        titulo = Text("Reservas Atuais", size=24, weight="bold")

        def cancelar_reserva_click(e, reserva):
            gerenciador.cancelar_reserva(reserva)
            alerta.content = Text("Reserva cancelada com sucesso.")
            alerta.open = True
            page.update()
            tela_reservas()

        lista_reservas = ListView(
            expand=True,
            spacing=5,
            auto_scroll=False,
            controls=[
                Column([
                    Text(r.exibir_informacoes()),
                    ElevatedButton("Cancelar Reserva", on_click=lambda e, r=r: cancelar_reserva_click(e, r))
                ], tight=True, spacing=2)
                for r in gerenciador.listar_reservas() if r.get_status() == "Ativa"
            ]
        )
        btn_voltar = ElevatedButton("Voltar", on_click=lambda e: tela_inicial())

        page.add(
            titulo,
            lista_reservas,
            btn_voltar
        )

    # Tela clientes
    def tela_clientes():
        page.clean()

        titulo = Text("Gerenciamento de Clientes", size=24, weight="bold")

        lista_clientes = ListView(
            expand=True,
            spacing=5,
            auto_scroll=False,
            controls=[
                Text(c.exibir_informacoes())
                for c in gerenciador.listar_clientes()
            ]
        )

        btn_voltar = ElevatedButton("Voltar", on_click=lambda e: tela_inicial())
        page.add(titulo, lista_clientes, btn_voltar)

    # Tela formulário reserva
    def tela_reserva():
        page.clean()

        titulo = Text("Nova Reserva", size=24, weight="bold")

        cliente_dropdown = Dropdown(
            label="Selecione Cliente",
            width=300,
            options=[
                DropdownMenuItem(text=f"{c.get_nome()} (ID: {c.get_id_cliente()})", key=c.get_id_cliente())
                for c in gerenciador.listar_clientes()
            ]
        )

        quarto_dropdown = Dropdown(
            label="Selecione Quarto",
            width=300,
            options=[
                DropdownMenuItem(text=q.exibir_informacoes(), key=q.get_numero())
                for q in gerenciador.quartos_disponiveis()
            ]
        )

        checkin_picker = DatePicker(label="Data Check-in", width=300)
        checkout_picker = DatePicker(label="Data Check-out", width=300)

        def criar_reserva_click(e):
            id_cliente = cliente_dropdown.value
            num_quarto = quarto_dropdown.value
            checkin = checkin_picker.value
            checkout = checkout_picker.value

            if not (id_cliente and num_quarto and checkin and checkout):
                alerta.content = Text("Por favor, preencha todos os campos.")
                alerta.open = True
                page.update()
                return

            # Converter datas para datetime
            try:
                checkin_dt = datetime.strptime(checkin, "%Y-%m-%d")
                checkout_dt = datetime.strptime(checkout, "%Y-%m-%d")
                if checkin_dt >= checkout_dt:
                    alerta.content = Text("Data de check-out deve ser maior que a de check-in.")
                    alerta.open = True
                    page.update()
                    return
            except Exception as ex:
                alerta.content = Text(f"Erro ao interpretar datas: {ex}")
                alerta.open = True
                page.update()
                return

            cliente = gerenciador.buscar_cliente_por_id(int(id_cliente))
            quarto = None
            for q in gerenciador.quartos_disponiveis():
                if q.get_numero() == int(num_quarto):
                    quarto = q
                    break

            if not quarto:
                alerta.content = Text("Quarto não está disponível.")
                alerta.open = True
                page.update()
                return

            reserva = gerenciador.criar_reserva(cliente, quarto, checkin_dt, checkout_dt)
            if reserva:
                alerta.content = Text("Reserva criada com sucesso!")
                alerta.open = True
                page.update()
                tela_inicial()
            else:
                alerta.content = Text("Falha ao criar reserva.")
                alerta.open = True
                page.update()

        btn_salvar = ElevatedButton("Salvar Reserva", on_click=criar_reserva_click)
        btn_voltar = ElevatedButton("Voltar", on_click=lambda e: tela_inicial())

        page.add(
            titulo,
            cliente_dropdown,
            quarto_dropdown,
            checkin_picker,
            checkout_picker,
            Row([btn_salvar, btn_voltar], alignment="spaceAround")
        )

    alerta = AlertDialog(title=Text("Aviso"), content=Text(""), actions=[ElevatedButton("OK", on_click=lambda e: setattr(alerta, "open", False))])
    page.dialog = alerta

    tela_inicial()
    page.update()

flet.app(target=main)

