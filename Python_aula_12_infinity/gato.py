# Crie outra classe chamada Gato que possua os mesmos atributos e
# o possua um método chamado derrubar coisas que retorna "O gato
# nome_do_gato quebrou algo". Faça a mesma impressão na tela
# para a classe gato.

class Gato:
    def __init__(self, nome, raca, peso):
        self.nome = nome
        self.raca = raca
        self.peso = peso
    
    def derrubar(self):
        return f"O {self.nome} derrubou algo"
    
gato1 = Gato(nome="Pipoca", raca="Pé duro", peso=0.8)

print(f"O {gato1.nome} é da raça {gato1.raca} pesa {gato1.peso}Kg e {gato1.derrubar()}")
