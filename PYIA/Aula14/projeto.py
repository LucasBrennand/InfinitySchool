class Cliente:
    def __init__(self, nome, telefone, email, id):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id = id

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, E-mail: {self.email}, ID: {self.id}"
    
class Quarto:
    def __init__(self, numero_quarto, tipo_quarto, preco_diaria, status):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto
        self.preco_diaria = preco_diaria
        self.status = status

    def __str__(self):
        return f"Numero do quarto: {self.numero_quarto}, Tipo de quarto{self.tipo_quarto}, Preço da diaria: {self.preco_diaria}, Status: {self.status}"

class Reserva:
    def __init__(self, dono, quarto_reservado, check_in, check_out, status):
        self.dono = dono
        self.quarto_reservado = quarto_reservado
        self.check_in = check_in
        self.check_out = check_out
        self.status = status

    def __str__(self):
        return f"Dono do quarto: {self.dono}, Reservado: {self.quarto_reservado}, Check-in: {self.check_in}, Check-out: {self.check_out}, Status: {self.status}"

class GerenciadorDeReserva:
    def __init__(self):
        self.quartos = []

    def criar_reserva(self, cliente, quarto):
        if quarto["status"] == "Disponivel":
            self.quartos.append(quarto)
    
    def modificar_reserva(self):
        return
    
    def cancelar_reserva(self):
        return

    def listar_reservas(self):
        return
    
    def listar_informacoes(self):
        return
    
class Main:
    cliente1 = Cliente("Lucas", "81995697350", "lucas12234567@gmail.com", 717)
    quarto1 = Quarto("101", "Deluxe", 300.00, "Disponivel")
    print(quarto1)