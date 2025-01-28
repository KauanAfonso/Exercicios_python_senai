class Loja_virtual:
    
    def __init__(self):
        self.produtos = []
        
    def criar_produtos(self,produto):
        dic = {"ID":produto.id , "NOME":produto.nome, "PRECOOOOOOO": produto.preco, "DESCRICAO": produto.descricao}
        self.produtos.append(dic)
        

    def mostrar_produtos(self):
        print(self.produtos)
        for produto in self.produtos:
            print(produto)
            
    def retornar_produtos(self):
        return self.produtos
           
    
class Produtos():
    def __init__(self, id, nome, preco, descricao):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
       
    def __str__(self):
        return f"ID {self.id} , {self.nome} custa R$ {self.preco} e sua decrição: {self.descricao}"
         
        
class carrinho_compras(Loja_virtual):
    def __init__(self):
        super().__init__()
        self.valor_total = 0
        self.produtos_no_carrinho = []
 
    
    def adicionar_produto(self):
        produ = self.retornar_produtos()
        for elemento in produ:
            print(elemento)
      
    
    def calcular_valor_total(self):
        pass
    
    
    

banana = Produtos(1,"banana",200,"Amarelo")
banana2 = Produtos(2,"banana 2",200,"amarelo")
minha_loja = Loja_virtual()

minha_loja.criar_produtos(banana)
minha_loja.criar_produtos(banana2)

# minha_loja.mostrar_produtos()
carrinho = carrinho_compras()
carrinho.adicionar_produto()
 
        
    
        