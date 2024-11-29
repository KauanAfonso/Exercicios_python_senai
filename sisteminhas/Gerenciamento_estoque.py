produtos = [
    ["Arroz" , "Feijão" , "Macarrão"],
    [0, 10, 8 ]
]

def remover_produto ():
    
    contador_produto_na_lista = 0
    
    for i , linha in enumerate(produtos):
       print(f"linha {i}: {linha}")
       
    nome = input("Qual produto você quer remover? ")
    quantidade = int(input("Qual quantidade você removerá? "))
    
    for i ,linha in enumerate(produtos):
        for j, elemento in enumerate(linha):      
            if elemento == nome:
                estoque = produtos[i + 1][j]
                contador_produto_na_lista += 1
                if estoque >= quantidade:
                    produtos[i + 1][j] = estoque - quantidade
                    print("Estoque atualizado")
                    break
                else:
                    print("não possui estoque suficiente !")
            else:
                continue
   
    if contador_produto_na_lista == 0:
        print("PRODUTO NÃO ENCONTRADO")

    print(produtos)
 


def editar_produto():
    contador_produto_na_lista = 0
    
    for i , linha in enumerate(produtos):
       print(f"linha {i}: {linha}")
       
    nome = input("Qual produto você quer alterar a quantidade? ")
    quantidade = int(input("Qual quantidade ele terá agora? "))

    for i, linha in enumerate(produtos):
        for j, elemento in enumerate(linha):
            if elemento == nome:
                produtos[i + 1][j] = quantidade
                print("Estoque atualizado")
                contador_produto_na_lista +=1
                break
    else:
        if contador_produto_na_lista < 1:
            print('Produto não encontrado !')
    print(produtos)



def visualizar_produtos():
   try:
    for i, produto in enumerate(produtos):  # Percorre as linhas de produtos
        for j, elemento in enumerate(produto):  # Percorre os elementos dentro da linha
            print(f"{j + 1} - Produto: {elemento} e Quantidade: {produtos[i + 1][j]}\n")  # Exibe o índice (j+1) e o nome do produto
   except:
       print("Acabaram os produtos")


def menu():
    while True:
        print('''
        
        Digite [1] - Vizualizar produtos
        Digite [2] - remover produtos
        Digite [3] - Editar quantidade    
        
        
        ''')
        valor = int(input("Digite um número : "))
        if valor == 1:
            visualizar_produtos()
        elif valor == 2:
            remover_produto()
        elif valor == 3:
            editar_produto()
        else:
            print("saindo...")
            break


menu()