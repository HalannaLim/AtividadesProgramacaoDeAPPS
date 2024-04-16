# Crie uma classe para implementar uma conta corrente.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente. Saque não realizado.")

    def _str_(self):
        return f"Conta {self.numero_conta} - Correntista: {self.nome_correntista}, Saldo: R${self.saldo}"


# Exemplo de uso da classe
conta1 = ContaCorrente(numero_conta="12345", nome_correntista="João")
print("Antes:", conta1)

conta1.deposito(1000)
conta1.saque(500)
conta1.alterarNome("João Silva")
print("Nome atualizado para: {}".format('João Silva'))
