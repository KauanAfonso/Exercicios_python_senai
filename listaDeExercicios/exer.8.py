palavra = input("Digite um palavra ai : ")
cont = 0
vogais = ['a' , 'e' , 'i' , 'o' ,'u', "A" , "E" , "I" , "O" , "U"]

for i in palavra:
    for j in vogais:
        if i == j:
            cont+=1
print(cont)