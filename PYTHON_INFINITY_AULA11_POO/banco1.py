# FAÇA UMA CLASSE CHAMADA CONTA BANCARIA COM OS SEGUINTES ATRIBUTOS:
# NOME DO TITULAR
# SALDO DA CONTA
# E AS SEGUINTES FUNÇÕES:
# DEPOSITAR (que aumenta o saldo)
# SACAR (que retira do saldo se for suficiente, se não
# mostra uma mensagem de saldo insuficiente)
# EXIBIR (que mostra o saldo atual)

class Conta_bancaria():
    #metodo construtor
    #a função __init__ serve para construir o objeto
    def __init__(self, nome_titular:str, saldo:float):
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self,deposito):
        self.saldo = self.saldo + deposito
        return f"Seu saldo é {self.saldo}"

    def sacar(self,saque):
        self.saldo = self.saldo - saque
        return f"Seu saldo é {self.saldo}"
    
nome_titular = str(input("Digite o nome do titular da conta: "))
saldo = float(input("Digite o saldo da conta: "))
deposito = float(input("Digite o valor a ser depositado: "))
saque = float(input("Digite o valor a ser sacado: "))

conta_bancaria1 = Conta_bancaria(nome_titular=nome_titular, saldo=saldo)

print(conta_bancaria1.depositar(deposito))
print(conta_bancaria1.sacar(saque))

