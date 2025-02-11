'''

Implemente uma classe chamada “Biblioteca” que represente uma biblioteca virtual. 
Essa classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar 
a disponibilidade de um livro.


'''

class Biblioteca:
    def __init__(self):
        self.livros_estoque = []
        self.listros_emprestados = []

    def cadastrar_livros(self, titulo, author, qtd):
        livro = {"titulo": titulo, "author":author , "Quantidade": qtd}
        return self.livros_estoque.append(livro)

    def fazer_emprestimos(self):
        pass
    
    def devolver_livros(self):
        pass

    def verificar_disponibilidade(self):
        pass