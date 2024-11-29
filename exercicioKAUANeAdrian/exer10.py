nota1 = float(input("Digite o valor da nota 1: "))
nota2 = float(input("Digite o valor da nota 2: "))
nota3 = float(input("Digite o valor da nota 3: "))

lista = []

lista.append(nota1)
lista.append(nota2)
lista.append(nota3)

nota_min = min(lista)
lista.remove(nota_min)

media = sum(lista) / 2

print(f"Sua média final é: {media}")

