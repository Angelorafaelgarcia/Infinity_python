# FAÇA UMA CLASSE CHAMADA TAMAGOTCHI

# ATRIBUTOS:
# nome
# saude
# energia
# METODOS:
# brincar
# lutar
# comer
# descansar

# brincar faz ele gastar 10 de energia
# lutar faz ele gastar 20 de energia
# comer faz ele recuperar 10 de energia
# descansar faz ele recuperar 20 de energia

class Tamagotchi:
    def __init__(self, nome:str, saude:int, energia:int):
        self.nome = nome
        self.saude = saude
        self.energia = energia
    
    def brincar(self):
        self.energia = self.energia - 10
        return self.energia

    def lutar(self):
        self.energia = self.energia - 20
        return self.energia
    
    def comer(self):
        self.energia = self.energia + 10
        return self.energia
    
    def descansar(self):
        self.energia = self.energia + 20
        return self.energia
        
nome = str(input("Digite o nome: "))
saude = int(input("Digite a saúde inicial: "))
energia = int(input("Digite a energia inicial: "))

tamagotchi1 = Tamagotchi(nome=nome, saude=saude, energia=energia)

while True:
    menu = int(input(f"""
            Bem vindo {tamagotchi1.nome}
            Saúde atual: {tamagotchi1.saude}
            Energia atual: {tamagotchi1.energia}

            1 - Brincar
            2 - Lutar
            3 - Comer
            4 - Descansar
            0 - Sair
    """))

    match menu:
        case 1:
            tamagotchi1.brincar()
        case 2:
            tamagotchi1.lutar()
        case 3:
            tamagotchi1.comer()
        case 4:
            tamagotchi1.descansar()
        case 0:
            break
        case _:
            print("Opção inválida")


