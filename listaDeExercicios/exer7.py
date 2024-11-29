num = input("Digite uma de numeros sepradros por espaço:")
lista = []
caracter = 0
somaTotal = 0

lista= num.split(' ')


for i in lista:
    somaTotal+= float(i)

print(somaTotal/ len(lista))

