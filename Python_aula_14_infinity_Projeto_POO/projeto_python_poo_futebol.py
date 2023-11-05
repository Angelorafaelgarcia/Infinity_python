# # Nesta aula vamos desenvolver um sistema para a FIFA.

# # A FIFA te contratou para desenvolver um sistema em Python para cadastro dos
# # times de um novo campeonato.

# # Nesse sistema deve ser possível cadastrar times, jogadores e comissão técnica.

# O sistema deve apresentar um menu para escolha de cadastro de jogador, time ou
# comissão técnica.

# # O sistema deve pedir para cadastro do time: O nome do time, a cidade onde o time
# # fará os jogos como mandante e o nome do mascote do time.

# # Para os jogadores, deverá ser possível cadastrar o nome do jogador, o nome do
# # time cujo ele atua, e o número da camisa.

# # Para a comissão técnica, teremos o técnico, o auxiliar e o preparador físico

# Para o técnico, o sistema deve cadastrar: O nome do técnico, o nome do time que
# ele comanda, e o esquema tático preferido (4-3-3 ou 4-4-2 por exemplo), o técnico
# deverá ter um método chamado dar_coletiva que retorna uma string: "O técnico
# está dando uma coletiva de imprensa".

# Para o auxiliar, deverá pedir os mesmos atributos e o método dar_coletiva retorna "O
# auxiliar está dando uma coletiva de imprensa".

# Para o preparador físico, o sistema deverá pedir o nome do preparador, o nome do
# time que ele prepara e, pedir qual parte do elenco ele prepara, "jogadores de linha"
# ou os "goleiros", deverá ter também o método dar_coletiva que retorna: "O
# preparador físico está dando uma coletiva de imprensa".

# Para desenvolver esse sistema, utilize todos os conceitos de programação
# orientada a objetos que foram estudados


class Time:
    def __init__(self, nome, cidade, mascote):
        self.__nome = nome
        self.__cidade = cidade
        self.__mascote = mascote

    def getNome(self):
        return self.__nome
    def setNome(self,novo_nome):
        self.__nome = novo_nome
        return self.nome

    def getCidade(self):
        return self.__cidade
    def setCidade(self,nova_cidade):
        self.__cidade = nova_cidade
        return self.cidade

    def getMascote(self):
        return self.__mascote
    def setMascote(self,novo_mascote):
        self.__mascote = novo_mascote
        return self.mascote

class Jogador:
    def __init__(self, nome, time, numero_camisa):
        self.__nome = nome
        self.__time = time
        self.__numero_camisa = numero_camisa

    def getNome(self):
        return self.__nome
    def setNome(self,novo_nome):
        self.__nome = novo_nome
        return self.nome

    def getTime(self):
        return self.__time
    def setTime(self,novo_time):
        self.__time = novo_time
        return self.time

    def getNumero_camisa(self):
        return self.__numero_camisa
    def setNumero_camisa(self,novo_numero_camisa):
        self.__numero_camisa = novo_numero_camisa
        return self.numero_camisa

class Comissao_tecnica:
    def __init__(self, nome, time, esquema_tatico):
        self.__nome = nome
        self.__time = time
        self.__esquema_tatico = esquema_tatico
        
    def dar_coletiva(self):
        return "Pode ser que algum membro da comissão esteja dando coletiva"
   
    def getNome(self):
        return self.__nome
    def setNome(self, novo_nome):
        self.__nome = novo_nome
        return self.nome
    
    def getTime(self):
        return self.__time   
    def setTime(self, novo_time):
        self.__time = novo_time
        return self.time
    
    def getFormacao(self):
        return self.__esquema_tatico   
    def setFormacao(self, novo_esquema_tatico):
        self.__esquema_tatico = novo_esquema_tatico
        return self.esquema_tatico


class Tecnico(Comissao_tecnica):
    def __init__(self, nome, time, esquema_tatico):
        super().__init__(nome, time, esquema_tatico)
    
    def dar_coletiva(self):
        return f"O técnico {self.getNome()} está dando coletiva"


class Auxiliar(Comissao_tecnica):
    def __init__(self, nome, time, esquema_tatico):
        super().__init__(nome, time, esquema_tatico)
    
    def dar_coletiva(self):
        return f"O auxiliar {self.getNome()} está dando coletiva"


class Preparador_fisico(Comissao_tecnica):
    def __init__(self, nome, time, parte_elenco):
        super().__init__(nome, time, parte_elenco)
        self.__parte_elenco = parte_elenco
    
    def getParteElenco(self):
        return self.__parte_elenco

    def setParteElenco(self, nova_parte_elenco):
        self.__parte_elenco = nova_parte_elenco
        return self.__parte_elenco
    
    def dar_coletiva(self):
        return f"O Preparador {self.getNome()} está dando coletiva"


while True:
    menu = int(input("""
            1 - Cadastrar Jogador
            2 - Cadastrar Time
            3 - Cadastrar Comissão Técnica
            4 - Sair
    """))

    match menu:
        case 1:
            nome = str(input("Digite o nome do jogador"))
            time = str(input("Digite o time do jogador"))
            numero_camisa = int(input("Digite o numero da camisa do jogador"))
            jogador = Jogador (nome=nome, time=time, numero_camisa=numero_camisa)
        case 2:
            nome = str(input("Digite o nome do time"))
            cidade_mandante = str(input("Digite da cidade como mandante"))
            mascote = str(input("Digite o nome do macote"))
            time = Time (nome=nome, cidade=cidade_mandante, mascote=mascote)
        case 3:
            while True:
                menu = int(input("""
                        1 - Cadastrar Tecnico
                        2 - Cadastrar Auxiliar
                        3 - Cadastrar Preparador Fisico
                        4 - Sair
                """))
                match menu:
                    case 1:
                        nome = str(input("Digite o nome do tecnico"))
                        time = str(input("Digite o time do tecnico"))
                        esquema_tatico = str(input("Digite o esquema tatico utilizado pelo tecnico"))
                        tecnico = Tecnico (nome=nome, time=time, esquema_tatico=esquema_tatico)
                    case 2:
                        nome = str(input("Digite o nome do auxiliar"))
                        time = str(input("Digite o time do auxiliar"))
                        esquema_tatico = str(input("Digite o esquema tatico utilizado pelo auxiliar"))
                        auxiliar = Auxiliar (nome=nome, time=time, esquema_tatico=esquema_tatico)
                    case 3:
                        nome = str(input("Digite o nome do preparador fisico"))
                        time = str(input("Digite o time do preparador fisico"))
                        parte_elenco = str(input("Digite qual parte do elenco ele prepara, ex: Jogadores de linha, goleiros... "))
                        preparador_fisico = Preparador_fisico (nome=nome, time=time, parte_elenco=parte_elenco)       
                    case 4:
                        print("Obrigado por usar o programa, tchau!")
                        break
                    case _:
                        print("Opção Inválida")
        case 4:
            print("Obrigado por usar o programa, tchau!")
            break
        case _:
            print("Opção Inválida")


