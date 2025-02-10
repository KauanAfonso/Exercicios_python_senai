'''
Implemente uma classe chamada “Livro” com atributos para armazenar o título, o 
autor e o número de páginas do livro. Adicione métodos para emprestar o livro, 
devolvê-lo e verificar se está disponível.

'''

class Livro():
    def __init__(self, titulo,autor,numero_paginas ):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.status = "Em estoque"
        
    def emprestar(self):
            self.status = "Emprestado"
        
    def devolver(self):
            self.status = "Em estoque"
            
    def verificar_livro(self):
        if self.status == "Em estoque":
            print("Livro disponível")
        else:
            print("Livro indisponível")


Simpson = Livro("Simpsons", "Kauan", 88)
Simpson.emprestar()
Simpson.verificar_livro()
    