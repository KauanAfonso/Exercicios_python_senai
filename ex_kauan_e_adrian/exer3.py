qtdProdutos = int(input("Digite a quantidade de produtos: "))
valorUnitario = float(input("Digite o valor unitário do produto: "))
valorTotal = qtdProdutos * valorUnitario

print("___________________________________________________________________________")

if qtdProdutos >= 100:
    desconto = valorTotal - (valorTotal * 0.10)
    print(f"O valor total é de: R$ {valorTotal}")
    print(f"O valor unitário é de: R$ {valorUnitario}")
    print(f"A quantidade de produtos é de : {qtdProdutos}")
    print(f"O valor com desconto de 10% é de: R$ {desconto}")
else:
    desconto = valorTotal - (valorTotal * 0.05)
    print(f"O valor total é de: R$ {valorTotal}")
    print(f"O valor unitário é de: R$ {valorUnitario}")
    print(f"A quantidade de produtos é de : {qtdProdutos}")
    print(f"O valor com desconto de 10% é de: R$ {desconto}")