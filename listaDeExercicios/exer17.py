num = input("Digite um número: ")
lista = []

for i in num:
    numero = int(i)
    lista.append(numero)
print(f"A soma dos números é de {sum(lista)}")