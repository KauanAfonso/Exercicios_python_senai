num = int(input("Digite um número:"))
contador = 0

if num <= 1 :
    print("Não é primo")
else:
    for i in range (2,num):
        if num % i == 0:
            contador += 1
if contador == 0:
    print("è numero primo")
else:
    print('não é')         