num = int(input("Digite um número: "))
i = 2
contador = 0

if num == 1:
    print('não pode ser primo')
else:
    while i < num:
        if num % i == 0:
            contador+= 1
        i+=1

if contador > 0:
    print('Não é primo')
else:
    print("é primo")