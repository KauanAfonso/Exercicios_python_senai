class Maquinas_vendas:
    def __init__(self, loja):
        self.nome_loja = loja
        self.produtos = []
        self.preco = 0
        self.nome_prod = 0
    
    def comprar(self,nome_produto):
        for produtos in self.produtos:
            print(produtos)
            for i in produtos:
                if i["Nome"] == nome_produto:
                    self.nome_prod = i["Nome"]
                    self.preco = i["Preco"]
                    i["Quantidade"] -= 1  
    
    def pagar(self, dinheiro):
        print(f"Seu produto é {self.nome_prod} , O valor é de {self.preco}")
        if dinheiro > self.preco:
            print(f"Seu troco é de {dinheiro - self.preco}")

    def visualizar_produtos(self):
        print(self.produtos)


class Produto(Maquinas_vendas):
    def __init__(self, nome, preco, loja, quant):
        super().__init__(loja)
        self.nome = nome
        self.preco = preco
        self.quant = quant
        self.criar_produto()

    def criar_produto(self):
        produto = [{"Nome": self.nome , "Preco": self.preco , "Quantidade":self.quant}]
        self.produtos.append(produto)
        

    def __str__(self):
        return f"Produto: {self.nome} , Preco {self.preco} , Quantidade {self.quant}"
    
loja = Maquinas_vendas("Kauan")
usrsinho = Produto("ursinho", 35, "Kauan", 12)
loja.visualizar_produtos()
loja.comprar("ursinho")
# loja.pagar(100)