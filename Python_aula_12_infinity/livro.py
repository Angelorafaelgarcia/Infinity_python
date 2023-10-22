# FAÇA UMA CLASSE CHAMADA LIVRO COM OS ATRIBUTOS:
# TITULO DO LIVRO
# AUTOR DO LIVRO
# GÊNERO DO LIVRO
# NÚMERO DE PÁGINAS
# E AS FUNÇÕES:
# EXIBIR INFORMAÇÕES COMPLETAS DO LIVRO (titulo, autor,
# genero, páginas)
# VERIFICAR SE O LIVRO É LONGO(considerar longo livros
# que contenha mais do que 350 páginas)


class Livro:
    def __init__(self, titulo:str, autor:str, genero:str, numero_paginas:int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.numero_paginas = numero_paginas
    
    def informacoes(self):
        return f"""
            Titulo: {self.titulo}
            Autor: {self.autor}
            Gênero: {self.genero}
            Número de Páginas: {self.numero_paginas}
        """
    def analise_paginas(self):
        if self.numero_paginas > 350:
            return f"O livro {self.titulo} é longo"
        else:
            return f"O livro {self.titulo} não é longo"

    
livro1 = Livro(titulo= "Senhor dos Aneis - As duas torres", autor="JRR Tolkien", genero="Aventura", numero_paginas=450)

print(livro1.informacoes())
print(livro1.analise_paginas())
