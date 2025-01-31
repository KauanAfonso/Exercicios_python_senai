class Loja_virtual:
    
    def __init__(self):
        self.produtos = []
        
    def criar_produtos(self,produto):
        dic = {"ID":produto.id , "NOME":produto.nome, "PRECO": produto.preco, "DESCRICAO": produto.descricao , "QUANTIDADE" : produto.quantidade}
        self.produtos.append(dic)
        

    def mostrar_produtos(self):
        print(self.produtos)
        for produto in self.produtos:
            print(produto)
                      
    
class Produtos():
    def __init__(self, id, nome, preco, descricao,qtd):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = qtd
       
    def __str__(self):
        return f"ID {self.id} , {self.nome} custa R$ {self.preco} e sua decrição: {self.descricao} e quantidade{self.quantidade}"
         
        
class carrinho_compras(Loja_virtual):
    def __init__(self, produtos = []):
        super().__init__()
        self.valor_total = 0
        self.produtos_no_carrinho = []
        self.produtos = produtos
 
    
    def adicionar_produto(self,nome_produto, quantidade):
        for elemento in self.produtos:
            if elemento["NOME"] == nome_produto:
                nome = elemento["NOME"]
                preco = elemento["PRECO"]
                quantidade_total = elemento["QUANTIDADE"]
                quantidade_total -= quantidade
                dic = {"Produto": nome, "Preco": {preco * quantidade}, "quantidade": quantidade}
                print('disponivel')
            else:
                print("erro")
            for i in elemento:
                print(i)
      
    
    def calcular_valor_total(self):
        pass   
    
    

banana = Produtos(1,"banana",200,"Amarelo" , 10)
banana2 = Produtos(2,"maça",200,"amarelo" , 8)

minha_loja = Loja_virtual()

minha_loja.criar_produtos(banana)
minha_loja.criar_produtos(banana2)

# minha_loja.mostrar_produtos()
carrinho = carrinho_compras(minha_loja.produtos)
carrinho.adicionar_produto("banana", 2)
 
        
    
        