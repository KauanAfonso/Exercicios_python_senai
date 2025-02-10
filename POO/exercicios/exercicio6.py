'''

Implemente uma classe chamada “Produto” que possua atributos para armazenar o 
nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor 
total em estoque e verificar se o produto está disponível. 


'''

class Produto:
    def __init__(self,nome, preco,quantidade):
        self.nome = nome 
        self.preco = preco
        self.quant = quantidade
        
    def valor_total(self):
        return self.preco * self.quant
    
    def verificar_disponibilidade(self):
        if self.quant >0:
            print("Diponivel")
        else:
            print("Indisponível")
            
    
batata = Produto("Batata", 50, 2)
batata.valor_total()
batata.verificar_disponibilidade()
        
        