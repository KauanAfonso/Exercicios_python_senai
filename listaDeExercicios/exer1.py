num = int(input("Digite um número:"))
sum = 0

for i in range(0, num+1, 2):
    sum+=i
print(f"A soma de todos os números pares de 1 até {num} é de {sum}")