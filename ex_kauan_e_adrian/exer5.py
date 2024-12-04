idade1 = int(input("Qual sua idade pessoa 1:"))
idade2 = int(input("Qual sua idade pessoa 2:"))
idade3 = int(input("Qual sua idade pessoa 3:"))

lista = []
lista.append(idade1)
lista.append(idade2)
lista.append(idade3)


MaiorIdade = max(lista)
menorIdade = min(lista)

print(f"A maior idade é de : {MaiorIdade} e a menor é de: {menorIdade}")
