soma_total = 0
nota = 0

for i in range(1, 6, 1):
    nota = float(input("Qual a nota do aluno? "))
    soma_total += nota

media = soma_total / i
print(f"Sua média é de {media}")

if media >= 5:
    print("Aprovado")
elif media >=2.5 and media < 5:
    print('Recuperação')
else:
    print("Reprovado")