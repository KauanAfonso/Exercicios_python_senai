notas = {}

for i in range(5):
    nome = input("Qual o nome: ")
    nota = float(input("digite a nota: "))
    
    notas[nome] = nota

melhor_aluno = max(notas ,key=notas.get)
print(melhor_aluno , notas[melhor_aluno])