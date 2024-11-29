num = int(input("Digite um número: "))
numNovo = str(num)
cont = 0
numerosImpares = ['1' , '3' , '5' , '7' ,'9']

for i in numNovo:
    for j in numerosImpares:
        if i == j:
            cont+=1

print(cont)