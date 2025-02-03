class Maquinas_vendas:
    def __init__(self):
        self.produtos = []
        self.preco = 0
        self.nome_prod = 0
    
    def comprar(self,nome_produto):
        for i in self.produtos:
            if i["Nome"] == nome_produto:
                self.nome_prod = i["Nome"]
                self.preco = i["Preco"]
                i["Quantidade"] -= 1  
    
    def pagar(self, dinheiro):
        print(f"Seu produto é {self.nome_prod} , O valor é de {self.preco}")


class Produto(Maquinas_vendas):
    def __init__(self, nome, preco, quant=0):
        super().__init__()
        self.nome = nome
        self.preco = preco
        self.quant = quant
        self.criar_produto(self)

    def criar_produto(self):
        produto = [{"Nome": self.nome , "Preco": self.preco , "Quantidade":self.quant}]
        self.produtos.append(produto)
        

    def __str__(self):
        return f"Produto: {self.nome} , Preco {self.preco} , Quantidade {self.quant}"
    
    