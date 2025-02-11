'''

Implemente uma classe chamada “Biblioteca” que represente uma biblioteca virtual. 
Essa classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar 
a disponibilidade de um livro.


'''

class Biblioteca:
    def __init__(self):
        self.livros_estoque = []
        self.listros_emprestados = []

    def cadastrar_livros(self, codigo,titulo, author, qtd):
        livro = {"codigo":codigo, "titulo": titulo, "author":author , "Quantidade": qtd}
        return self.livros_estoque.append(livro)

    def fazer_emprestimos(self,nome,email, codigo_livro, quantidade):
        for livro in self.livros_estoque:
            if livro["codigo"] == codigo_livro and livro["Quantidade"] > 0 and livro["Quantidade"]>= quantidade:
                livro["Quantidade"] -= quantidade
                self.listros_emprestados.append(f"Empréstimo para {nome} no email {email} Código: {livro['codigo']}, título: {livro['titulo']}, autor: {livro['author']} quantidade: {quantidade}")
                break
            else:
                "indiponível"
        else:
            "livro não encontrado"

    
    def devolver_livros(self):
        pass

    def verificar_disponibilidade(self):
        pass



bibliotea = Biblioteca()
bibliotea.cadastrar_livros(1234, "O pé grande", "Kauan Afonso", 20)
bibliotea.fazer_emprestimos("Kauan", "kuan@gmail.com", 1234, 2)
print(bibliotea.lz)