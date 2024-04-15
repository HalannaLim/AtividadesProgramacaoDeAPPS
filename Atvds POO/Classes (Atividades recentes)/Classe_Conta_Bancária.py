import time

class Conta_bancaria:
    def __init__(self, titular, saldo, limite_emprestimo, numero):
        self.titular = titular
        self.saldo = saldo
        self.limite_emprestimo = limite_emprestimo
        self.numero = numero
        self.conta_ativa = False
        self.transacoes = []

    def sacar(self, saque):
        if self.conta_ativa and (self.saldo + self.limite_emprestimo) >= saque:
            print(f'{self.titular} está sacando R$: {saque}')
            self.saldo -= saque
            self.transacoes.append(f"Saque de R$ {saque}")
        else:
            print("Operação não permitida.")

    def depositar(self, deposito):
        if self.conta_ativa:
            print(f'{self.titular} está depositando R$: {deposito}')
            self.saldo += deposito
            self.transacoes.append(f"Depósito de R$ {deposito}")
        else:
            print("Operação não permitida.")

    def menu(self):
        while True:
            print("""
        ★                                   Bem vindo ao Menu                                     ★
        ★                                                                                         ★
        ★  1. Vizualizar saldo                                      6. Desbloquear conta          ★
        ★  2. Mudar limite                                           7. Extrato da conta           ★
        ★  3. Depositar                                              8. Pagamento de contas        ★
        ★  4. Realizar saque                                         9. Investir                   ★
        ★  5. Bloquear conta                                                                       ★
        ★  0. Sair do programa                                                                     ★
        ★                                                                                         ★
        ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★""")
            opcao = input("\n        Escolha uma opção do menu: ")

            if opcao == '1':
                self.verificar_saldo()
            elif opcao == '2':
                novo_limite = float(input("Digite o novo limite de empréstimo: "))
                self.mudar_limite_emprestimo(novo_limite)
            elif opcao == '3':
                valor_deposito = float(input("Digite o valor a ser depositado: "))
                self.depositar(valor_deposito)
            elif opcao == '4':
                valor_saque = float(input("Digite o valor a ser sacado: "))
                self.sacar(valor_saque)
            elif opcao == '5':
                self.bloqueio()
            elif opcao == '6':
                self.desbloqueio()
            elif opcao == '7':
                self.extrato()
            elif opcao == '8':
                valor_conta = float(input("Digite o valor da conta a ser paga: "))
                self.pagar_conta(valor_conta)
            elif opcao == '9':
                valor_investimento = float(input("Digite o valor a ser investido: "))
                self.investir(valor_investimento)
            elif opcao == '0':
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    def verificar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")

    def mudar_limite_emprestimo(self, novo_limite):
        self.limite_emprestimo = novo_limite
        print("Limite de empréstimo alterado com sucesso.")

    def bloqueio(self):
        self.conta_ativa = False
        print("Conta bloqueada.")

    def desbloqueio(self):
        self.conta_ativa = True
        print("Conta desbloqueada.")

    def extrato(self):
        print("Transações:")
        for transacao in self.transacoes:
            print(transacao)

    def pagar_conta(self, valor_conta):
        if self.conta_ativa and self.saldo >= valor_conta:
            print(f"Conta de R$ {valor_conta} paga.")
            self.saldo -= valor_conta
            self.transacoes.append(f"Pagamento de conta de R$ {valor_conta}")
        else:
            print("Operação não permitida.")

    def investir(self, valor_investimento):
        if self.conta_ativa and self.saldo >= valor_investimento:
            print(f"R$ {valor_investimento} investidos.")
            self.saldo -= valor_investimento
            self.transacoes.append(f"Investimento de R$ {valor_investimento}")
        else:
            print("Operação não permitida.")

titular = input("Digite o nome do titular: ")
saldo = float(input("Digite o saldo da sua conta: "))
limite_emprestimo = float(input("Digite o seu limite de empréstimo: "))
numero = input("Digite o número da sua conta: ")

conta = Conta_bancaria(titular, saldo, limite_emprestimo, numero)

print(f"\nBem-vindo, {titular}!")
conta.menu()
