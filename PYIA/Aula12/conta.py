class Conta:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor_deposito):
        self.saldo = self.saldo + valor_deposito
        print(f"O seu novo saldo é R${self.saldo}")
    
    def saque(self, valor_saque):
        saldo_atual = 0
        
        if (self.saldo > 0):
            saldo_atual = self.saldo - valor_saque
            if (saldo_atual >= 0):
                print(self.saldo)
                self.saldo = saldo_atual
                print(f"O seu novo saldo é R${self.saldo}")
            else:
                print("Saldo insuficiente para esse saque")
        else:
            print("Saldo zerado")
    
    def resumo(self):
        print(f"O seu saldo é R${self.saldo}")

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, saldo):
        super().__init__(numero_conta, titular, saldo)

    def resumo(self):
        print(f"O seu saldo é R${self.saldo}")

conta1 = Conta(123,"Lucas", 2000)
conta1.resumo()
conta1.saque(2000)
conta1.resumo()
conta1.saque(3000)
conta1.deposito(1000)
