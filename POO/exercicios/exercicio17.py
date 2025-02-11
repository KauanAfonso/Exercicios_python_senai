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
        livro = {"codigo":codigo, "titulo": titulo, "author":author , "quantidade": qtd}
        return self.livros_estoque.append(livro)

    def fazer_emprestimos(self,nome,email, codigo_livro, quantidade):
        for livro in self.livros_estoque:
            if livro["codigo"] == codigo_livro and livro["quantidade"] > 0 and livro["quantidade"]>= quantidade:
                livro["quantidade"] -= quantidade
                self.listros_emprestados.append({"nome": nome, "email": email, "codigo": livro["codigo"], "titulo": livro["titulo"], "autor": livro["author"], "quantidade": quantidade})
                break
            else:
                return "indiponível"
        else:
            return "livro não encontrado"

    
    def devolver_livros(self, codigo):
        quant = 0
        for livro in self.listros_emprestados:
            if livro["codigo"] == codigo:
                quant = livro["quantidade"]
                self.listros_emprestados.remove(livro)

                for livro in self.livros_estoque:
                    if livro["codigo"] == codigo:
                        livro["quantidade"] += quant
            else:
                return 'Não encontrado'


    def verificar_disponibilidade(self, codigo):
        for livro in self.livros_estoque:
            print(livro['codigo']) 
            if livro['codigo'] == codigo and livro["quantidade"] > 0:
                return "Disponível"
            else:
                print("Não disponível")



bibliotea = Biblioteca()
bibliotea.cadastrar_livros(1234, "O pé grande", "Kauan Afonso", 20)
bibliotea.fazer_emprestimos("Kauan", "kuan@gmail.com", 1234, 1)

print(bibliotea.livros_estoque)
bibliotea.devolver_livros(1234)
# print(bibliotea.livros_estoque)

print(bibliotea.verificar_disponibilidade(1234))