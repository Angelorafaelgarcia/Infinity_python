# Crie uma classe chamada Cachorro que possua 3 atributos: nome,
# raça e peso. Implemente um método: comer ração, que retorna
# "croc croc croc".

# Crie duas instâncias dessa classe, e imprima na tela: "O cachorro
# nome_do_cachorro é da raça raça_do_cachorro, pesa
# peso_do_cachorro quilos e come: croc croc croc".

class Cachorro:
    def __init__(self, nome, raca, peso):
        self.nome = nome
        self.raca = raca
        self.peso = peso

    def comer(self):
        return "croc croc croc"
    

cachorro1 = Cachorro(nome="Princesa", raca="Pinsher", peso=40)
cachorro2 = Cachorro(nome="Pudim", raca="Shi tzu", peso=5)

print(f"O cachorro {cachorro1.nome} é da raça {cachorro1.raca}, pesa {cachorro1.peso} quilos e come: {cachorro1.comer()}")
print(f"O cachorro {cachorro2.nome} é da raça {cachorro2.raca}, pesa {cachorro2.peso} quilos e come: {cachorro2.comer()}")
