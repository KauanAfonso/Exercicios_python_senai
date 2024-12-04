lado1 = float(input("Digite o tamanho do comprimento de cima: "))
lado2 = float(input("Digite o tamanho da altura da direita: "))
lado3 = float(input("Digite o tamanho do comprimento de baixo: "))
lado4 = float(input("Digite o tamanho da altura da esquerda: "))

if lado1 == lado3 and lado2 == lado4 and lado1 != lado2 :
    print("É um retângulo!")
elif lado1 == lado3 and lado2 == lado4 and lado1 == lado2 :
    print("É um quadrado!")
else :
    print("Não é um quadrado nem um retângulo!")