import random 

num_aleatorio = random.randint(1, 10)
numero = int(input("Digite um numero:"))

if numero == num_aleatorio:
    print("Acertou o número, o numero era: " , num_aleatorio)
else:   
    while(numero != num_aleatorio):        
        if numero > num_aleatorio:
            print("O numero aletorio é menor !")
        elif numero < num_aleatorio:
            print("O numero aletorio é maior !")

        numero = int(input("Digite um numero:"))
        
    print("Acertou o número, o numero era: " , num_aleatorio)