qtd = int(input("DIgite a quantidade de notas: "))
soma = 0

for qntd in range(0, qtd):
    nota = float(input("Digite a nota: "))
    soma = soma + nota
print(f"A media é de {soma/qtd}")