#Primeiro teste orientado a objetos em Python

class ContaBancaria:
    def __init__(self, numero_da_conta, nome_titular, saldo):
        self.conta = numero_da_conta
        self.titular = nome_titular
        self.saldo = saldo

    def depositar(self):
        valor = float(input("Quanto você deseja depositar? "))
        self.saldo = self.saldo + valor
        print(f"Depósito de R${valor:.2f} reais realizado! Novo saldo: R${self.saldo:.2f}")

    def sacar(self):
        saque = float(input("Quanto você deseja sacar? "))
        if saque > self.saldo:
            print("Valor do saque maior que o saldo disponível! Digite um valor menor ou igual ao saque.")
        else:
            self.saldo = self.saldo - saque
            print(f"Saque de R${saque:.2f} realizado com sucesso! Novo saldo: R${self.saldo:.2f}")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

conta_do_joao = ContaBancaria(1234, "João da Silva", 500.0) 

conta_do_joao.depositar()
conta_do_joao.sacar()
conta_do_joao.verificar_saldo()