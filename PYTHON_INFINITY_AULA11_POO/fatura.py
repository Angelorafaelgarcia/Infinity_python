
class Fatura():
    #metodo construtor
    #a função __init__ serve para construir o objeto
    def __init__(self, produto:str, preco:float, quantidade:int):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade
     
    
    def total(self):
        return f"O Valor total da fatura foi: {self.preco*self.quantidade}"

    
produto = str(input("Nome do produto: "))
preco = float(input("Digite o valor: "))
quantidade = int(input("Digite a quantidade: "))

fatura1 = Fatura(produto=produto, preco=preco, quantidade=quantidade)

print(fatura1.total())


