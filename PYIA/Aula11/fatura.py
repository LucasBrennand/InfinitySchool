class Fatura:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def gerar_fatura(self):
        total = self.preco * self.quantidade
        print(f"O total deu R${total}")
        return total
    
fatura = Fatura("Banana", 2.00, 50)
fatura.gerar_fatura()