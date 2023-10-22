# Pense em sistema bancário, nesse sistema há 2 contas: conta-corrente e conta
# poupança.

# Ambas possuem um identificado numérico, nome do titular e saldo. Possuem
# também dois métodos: verificar informações, que retorna todas as informações
# daquela conta e, depósito, que adiciona determinado valor ao saldo daquela
# conta.

# Apenas a conta-corrente possui também o método sacar que subtrai
# determinado valor da conta.

# Apenas a conta poupança possui também um atributo chamado juros.

# Quem utilizará esse sistema é um gerente, portanto, o sistema deve permitir que
# ele crie uma conta-correte ou conta poupança nova e, que consiga utilizar
# todas as funções.


class Conta:
    def __init__(self, id:int, nome:str, saldo:float):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def visualizar_infos(self):
        return f"""
            Identificador: {self.id}
            Nome do Títular: {self.nome}
            Saldo da conta: {self.saldo}
        """
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
class Corrente(Conta):
    def __init__(self, id: int, nome: str, saldo: float):
        super().__init__(id, nome, saldo)

        def sacar(self, valor):
            self.saldo = self.saldo - valor
            return self.saldo
        
class Poupanca(Conta):
    def __init__(self, id: int, nome: str, saldo: float, juros:float):
        super().__init__(id, nome, saldo)
        self.juros = juros



while True:
    menu = int(input("""
            Bem vindo
            1 - Criar conta Corrente
            2 - Criar conta Poupança
            0 - Sair
    """))

    match menu:
        case 1:
            identificador = int(input("Digite o id: "))
            nome = str(input("Digite o nome do títular: "))
            saldo = float(input("Digite o saldo inicial: "))

            conta1 = Corrente(id=identificador, nome=nome, saldo=saldo)

        case 2:

            identificador = int(input("Digite o id: "))
            nome = str(input("Digite o nome do títular: "))
            saldo = float(input("Digite o saldo inicial: "))
            juros = float(input("Digite o juros: "))

            conta2 = Poupanca(id=identificador, nome=nome, saldo=saldo, juros=juros)
        case 0:
            break

        case _:
            print("Opção Inválida")

