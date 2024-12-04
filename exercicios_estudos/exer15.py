numero_primo = 8
i = 2
contagem_divisao =0
if numero_primo <=1:
    print("Não é primo !")
else:
     while i < numero_primo:
        if numero_primo % 2 == 0:
            contagem_divisao+=1
        i+=1

if contagem_divisao >0:
     print('Não é primo')
else:
     print("Primo !")