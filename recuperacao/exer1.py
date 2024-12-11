
lista_produtos = []

contador_situacao_em_falta = 0
contador_situacao_em_estoque_medio = 0
contador_situacao_em_estoque_abundante = 0

quantidade = int(input("Qual a quantidade de produtos? "))
i = 0

while i < quantidade:

    produto = []

    nome = input("Qual o nome do produto? ")
    codigo = int(input("Qual o codigo do produto? "))
    quantidade_produto = int(input("Qual a quantidade em estoque? "))
    preco = float(input("Qual o preco do produto: "))

    produto.append(nome)
    produto.append(codigo)
    produto.append(quantidade_produto)
    produto.append(preco)
 
    if produto[2] <= 5:
        produto.append("Em falta")
        contador_situacao_em_falta +=1

    elif produto[2] > 5 and produto[2] <= 20:
        produto.append("Estoque médio")
        contador_situacao_em_estoque_medio+=1

    else:
         produto.append("Estoque Abundante")
         contador_situacao_em_estoque_abundante+=1

    lista_produtos.append(produto)

    i+=1
    print(i)

print("------------------------Seus Produtos:------------------------------")
print(lista_produtos)
print("------------------------Quantidade por categoria:---------------------")
print(f"Em falta {contador_situacao_em_falta}\n Estoque médio {contador_situacao_em_estoque_medio}\n Estoque abundante {contador_situacao_em_estoque_abundante}")


