class Cachorro:
    def __init__(self,nome,raca,cor,idade):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.orelhas = 2
        
    def latir(self):
        print("au au")
        
    def correr(self, km):
        print(f"{self.nome} correu {km} km")
        


cachorro_luana = Cachorro("Pituco", "Vira-lata" , "Caramelo", 8)
cachorro_luana.correr(35)


class Livro:
    def __init__(self, categoria, titulo, autor,personagens, indicados):
        self.genero = categoria
        self.titulo = titulo
        self.autor = autor
        self.personagens = personagens
        self.indicados = indicados
        
    def abrir(self, pagina):
        print(f"O livro {self.titulo} foi aberto na {pagina}")
        
    def __str__(self):#retornar o livro
        return f"O livro {self.titulo} foi escrito por {self.autor}"
    
    def __eq__(self, value):
        if (isinstance(value, Livro)):
            titulo_igual = self.titulo == value.titulo
            autores_iguais = self.autor == value.autor
            return titulo_igual and autores_iguais
        else:
            return False
        
        

livro1 = Livro("Romance", "Crepusculo", "kauan afonso", ["Teddy", "Lucas"], 14)
livro1.abrir(10)
print(livro1.__eq__(cachorro_luana))
print(livro1)