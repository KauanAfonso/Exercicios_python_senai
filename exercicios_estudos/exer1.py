#Crie um algorimo que receba 10 numero e retorne quantos sao pares

numeros = []
contador = 0

for i in range (0, 10):
    num_digitado = float(input('Digite um número: '))
    numeros.append(num_digitado)
    
for i in numeros:
    if i % 2 ==0:
        contador += 1

print(f" A lista {numeros} tem {contador} numeros pares !")