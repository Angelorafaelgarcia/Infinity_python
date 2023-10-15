class Carro():
    #metodo construtor
    #a função __init__ serve para construir o objeto
    def __init__(self, marca:str, modelo:str, ano:int, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_inicial = 0
    
    def ligar(self):
        return f"Você ligou o {self.modelo}"

    def acelerar(self,velocidade):
        self.velocidade_inicial = self.velocidade_inicial + velocidade
        return f"Acelerou o {self.marca} que está a {self.velocidade_inicial} km/h"
    


marca = str(input("Digite a marca: "))
modelo = str(input("Digite o modelo: "))
ano = int(input("Digite o ano: "))
cor = str(input("Digite a cor: "))

carro1 = Carro(marca=marca, modelo=modelo, ano=ano, cor=cor)

print(carro1.ligar())
print(carro1.acelerar(30))
print(carro1.acelerar(150))
print(carro1.velocidade_inicial)